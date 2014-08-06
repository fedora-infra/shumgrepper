# -*- coding:utf-8 -*-
import flask
import fedmsg
import fedmsg.meta

from math import ceil
import summershum.model as sm

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

import shumgrepper.api

from shumgrepper.doc_utils import load_docs

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

    return flask.redirect(flask.url_for('.list_all_packages',
                                            motif=search_term))

# list the names of packages
@app.route('/packages')
@app.route('/packages/<motif>/')
def list_all_packages(motif=None):
    pattern = flask.request.args.get('motif', motif) or '*'
    limit = flask.request.args.get('limit', app.config['ITEMS_PER_PAGE'])
    page = flask.request.args.get('page', 1)

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
    )

    packages_count = sm.File.get_all_packages(
        session,
        pattern=pattern,
        limit=limit,
        count=True,
        page=page,
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
        packages = packages,
        page=page,
        total_page=total_page
    )


# request files by sha1sum
@app.route('/sha1/<sha1>')
def sha1sum(sha1):
    messages = sm.File.by_sha1(session, sha1)
    msg_list = JSONEncoder(messages)

    return flask.render_template(
            'files.html',
            all_files=msg_list
    )


# request files by md5sum
@app.route('/md5/<md5>')
def md5sum(md5):
    messages = sm.File.by_md5(session, md5)
    msg_list = JSONEncoder(messages)

    return flask.render_template(
        'files.html',
        all_files=msg_list
    )


# request files by sha256sum
@app.route('/sha256/<sha256>')
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
@app.route('/tar_file/<tar_file>/filenames')
def tar_file_filenames(tar_file):
    messages = sm.File.by_tar_file(session, tar_file)

    file_list = []
    for message in messages:
        file_list.append(message.filename)

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
    messages = sm.File.package_filenames(session, package)

    return flask.render_template(
        'package_filename.html',
        all_files=file_list,
        count=len(file_list),
    )


# returns the versions available for a package
@app.route('/package/<package>')
def package(package):
    messages = sm.File.by_package(session, package)
    file_list = []
    for message in messages:
        file_list.append(message.tar_file)

    file_list = set(file_list)
    return flask.render_template(
        'package.html',
        all_files=file_list,
        count=len(file_list),
    )


#compare and return filenames different in all tar_files
@app.route('/compare')
@app.route('/compare/difference')
def compare_difference():
    tar_files = flask.request.args.getlist('tar_file', None)

    messages_list = []
    for tar_file in tar_files:
        messages = sm.File.by_tar_file(session, tar_file)
        if messages:
            messages = to_dict(messages)
            messages_list.append(messages)

    # calculate uncommon sha256sum
    common_sha256 = set.intersection(*map(set, messages_list))
    uncommon_sha256 = []
    for messages in messages_list:
        diff = set(messages.keys()) - set(common_sha256)
        for sha256 in diff:
            uncommon_sha256.append(sha256)

    # calculate final results
    length = len(tar_files)
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
        all_files = results,
        compared_values = tar_files,
        length = length,
    )


#compare and return filenames common in tar_files
@app.route('/compare/common')
def compare_common():
    tar_files = flask.request.args.getlist('tar_file', None)
    messages_list = []
    for tar_file in tar_files:
        messages = sm.File.by_tar_file(session, tar_file)
        if messages:
            messages = to_dict(messages)
            messages_list.append(messages)

    # calculate common sha256 sum in messages_list
    common_sha256 = set.intersection(*map(set, messages_list))

    # calculate final results
    length = len(tar_files)
    results = []
    for sha256 in common_sha256:
        result = []
        for i in range(length):
            if sha256 in messages_list[i]:
                result.append(messages_list[i][sha256])
        result.append(sha256)
        results.append(result)

    return flask.render_template(
        'compare.html',
        all_files = results,
        compared_values = tar_files,
        length = length,
    )


# returns history of a package
@app.route('/history/<package>')
def history(package):
    messages = sm.File.by_package(session, package)
    versions = []
    for message in messages:
        versions.append(message.tar_file)

    versions = set(versions)
    versions =  list(versions)

    sha256_list = []
    messages_list = []
    for version in versions:
        messages = sm.File.by_tar_file(session, version)
        if messages:
            msg_dict = {}
            for message in messages:
                msg_dict[message.sha256sum] = message.filename
                sha256_list.append(message.sha256sum)
            messages_list.append(msg_dict)
    sha256_list = set(sha256_list)
    sha256_list = list(sha256_list)

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
        results = results,
        versions = versions,
        length = len(versions),
    )

# return packages having atleast a file matching the pattern
@app.route('/pattern/<pattern>')
def pattern(pattern):
    packages = sm.File.get_all_packages(
        session,
        pattern='*',
    )

    package_list = []
    for package in packages:
        files = sm.File.file_filter(session, package[0], pattern)
        if files:
            package_list.append(package[0])

    return flask.render_template(
            'pattern.html',
            all_files=package_list,
    )

