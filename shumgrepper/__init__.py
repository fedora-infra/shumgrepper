# -*- coding:utf-8 -*-
import flask
import fedmsg
import fedmsg.meta

from math import ceil
import summershum.model as sm
from shumgrepper.doc_utils import load_docs

from shumgrepper.util import (
    JSONEncoder,
    to_dict
)

app = flask.Flask(__name__)

fedmsg_config = fedmsg.config.load_config()
fedmsg.meta.make_processors(**fedmsg_config)

session = sm.create_session(
    fedmsg_config['summershum.sqlalchemy.url'],
    create=True,
    )

app.config.from_object('default_config')


@app.route('/')
def home():
    return flask.render_template(
        'home.html',
        docs=load_docs(flask.request)

    )


@app.route('/search/')
def search():
    ''' Redirect to the correct url to perform the appropriate search.
    '''
    search_term = flask.request.args.get('term', '*') or '*'

    if not search_term.endswith('*'):
        search_term += '*'

    return flask.redirect(
        flask.url_for(
            '.list_all_packages',
            motif=search_term
        )
    )


# list the names of packages
@app.route('/packages')
@app.route('/packages/<motif>/')
def list_all_packages(motif=None, origin='list_all_packages', extension=None):
    pattern = flask.request.args.get('motif', motif) or '*'
    limit = flask.request.args.get('limit', app.config['ITEMS_PER_PAGE'])
    page = flask.request.args.get('page', 1)
    extension = flask.request.args.get('extension', None)

    try:
        page = abs(int(page))
    except ValueError:
        page = 1

    try:
        limit = abs(int(limit))
    except ValueError:
        limit = app.config['ITEMS_PER_PAGE']
        flask.flash('Incorrect limit provided, using default', 'errors')

    packages = sm.File.get_all_packages(
        session,
        pattern=pattern,
        limit=limit,
        page=page,
        extension=extension,
    )

    packages_count = sm.File.get_all_packages(
        session,
        pattern=pattern,
        limit=limit,
        count=True,
        page=page,
        extension=extension,
    )

    total_page = int(ceil(packages_count / float(limit)))

    packages = [pkg[0] for pkg in packages]

    if len(packages) == 1:
        flask.flash(
            'Only one package matching, redirecting you to its page')
        return flask.redirect(flask.url_for(
            '.package', package=packages[0]))

    return flask.render_template(
        'list_all_packages.html',
        packages=packages,
        packages_count=packages_count,
        page=page,
        total_page=total_page,
        origin=origin,
        extension=extension
    )


# request files by sha1sum
@app.route('/sha1/<sha1>')
@app.route('/sha1sum/<sha1>')
def sha1sum(sha1):
    messages = sm.File.by_sha1(session, sha1)
    msg_list = JSONEncoder(messages)

    return flask.render_template(
        'files.html',
        all_files=msg_list
    )


# request files by md5sum
@app.route('/md5/<md5>')
@app.route('/md5sum/<md5>')
def md5sum(md5):
    messages = sm.File.by_md5(session, md5)
    msg_list = JSONEncoder(messages)

    return flask.render_template(
        'files.html',
        all_files=msg_list
    )


# request files by sha256sum
@app.route('/sha256/<sha256>')
@app.route('/sha256sum/<sha256>')
def sha256sum(sha256):
    messages = sm.File.by_sha256(session, sha256)
    msg_list = JSONEncoder(messages)

    return flask.render_template(
        'files.html',
        all_files=msg_list,
    )


# request files by tarsum
@app.route('/tar_sum/<tar_sum>')
def tar_sum(tar_sum):
    messages = sm.File.by_tar_sum(session, tar_sum)
    msg_list = JSONEncoder(messages)

    return flask.render_template(
        'files.html',
        all_files=msg_list
    )


# request files by tarsum
@app.route('/tarball/<tarball>/filenames')
def tarball_filenames(tarball):
    messages = sm.File.by_tarball(session, tarball)

    file_list = map(lambda x: x.filename, messages)

    return flask.render_template(
        'package_filename.html',
        all_files=file_list,
        count=len(file_list),
    )


# request files data by filename
@app.route('/filename/<path:filename>')
def filename(filename):
    filename = '/' + filename

    messages = sm.File.by_filename(session, filename)
    msg_list = JSONEncoder(messages)

    return flask.render_template(
        'files.html',
        all_files=msg_list
    )


# list filenames present in a package
@app.route('/package/<package>/filenames')
def package_filenames(package):
    filenames = sm.File.package_filenames(session, package)

    filename_list = [filename[0][1:] for filename in filenames]

    return flask.render_template(
        'package_filename.html',
        all_files=filename_list,
        count=len(filename_list),
    )


# returns the versions available for a package
@app.route('/package/<package>')
def package(package):
    tarball_list = sm.File.package_tarball(session, package)

    tarball_list = [tarball[0] for tarball in tarball_list]

    return flask.render_template(
        'package.html',
        all_files=tarball_list,
        count=len(tarball_list),
        package=package,
    )


# compare and return filenames different in all tarballs
@app.route('/compare')
@app.route('/compare/difference')
def compare_difference():
    tarballs = flask.request.args.getlist('tarball', None)

    messages_list = filter(lambda x:bool(sm.File.by_tarball(session, x)), tarballs)

    common_sha256 = set.intersection(*map(set, messages_list))

    # calculate uncommon sha256sum
    uncommon_sha256 = map(lambda x: set(x.keys())-set(common_sha256), messages_list)

    # calculate final results
    length = len(tarballs)
    results = []
    for sha256 in uncommon_sha256:
        result = []
        for i in range(length):
            if sha256 in messages_list[i]:
                result.append(messages_list[i][sha256])
            else:
                result.append(" ")
        result.append(sha256)
        results.append(result)

    return flask.render_template(
        'compare.html',
        all_files=results,
        compared_values=tarballs,
        length=length,
    )


# compare and return filenames common in tarballs
@app.route('/compare/common')
def compare_common():
    tarballs = flask.request.args.getlist('tarball', None)

    messages_list = filter(lambda x:to_dict(bool(sm.File.by_tarball(session, tarball))), tarballs)

    # calculate common sha256 sum in messages_list
    common_sha256 = set.intersection(*map(set, messages_list))

    # calculate final results
    results = []
    for sha256 in common_sha256:
        result = []
        for i in range(len(tarballs)):
            if sha256 in messages_list[i]:
                result.append(messages_list[i][sha256])
        result.append(sha256)
        results.append(result)

    return flask.render_template(
        'compare.html',
        all_files=results,
        compared_values=tarballs,
        length=len(tarballs),
    )


# returns history of a package
@app.route('/history/<package>')
def history(package):
    messages = sm.File.by_package(session, package)

    versions = list(set(map(lambda x: x.tarball, messages)))

    sha256_list = []
    messages_list = []
    for version in versions:
        messages = sm.File.by_tarball(session, version)
        if messages:
            msg_dict = {}
            for message in messages:
                msg_dict[message.sha256sum] = message.filename
                sha256_list.append(message.sha256sum)
            messages_list.append(msg_dict)
    sha256_list = list(set(sha256_list))

    results = []
    for sha256 in sha256_list:
        result = []
        for messages in messages_list:
            if sha256 in messages:
                result.append(messages[sha256])
            else:
                result.append(" ")
        result.append(sha256)
        results.append(result)

    return flask.render_template(
        "history.html",
        results=results,
        versions=versions,
        length=len(versions),
    )

import shumgrepper.api
