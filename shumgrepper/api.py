import json
import flask

import summershum.model as sm
from shumgrepper import app, session
from shumgrepper.util import (
    JSONEncoder,
    to_dict
)

from shumgrepper.doc_utils import load_docs


@app.route('/api')
def api():

    return flask.render_template(
        'api.html',
        docs=load_docs(flask.request)
    )


@app.route('/api/packages')
def api_packages():
    packages = sm.File.packages(session)
    package_list = []
    for package in packages:
        package_list.append(package[0])

    return flask.Response(
        response=json.dumps(package_list),
        mimetype="application/json",
    )


@app.route('/api/sha1/<sha1>')
@app.route('/api/sha1sum/<sha1>')
def api_sha1sum(sha1):
    messages = sm.File.by_sha1(session, sha1)
    # converts message into list of dict
    msg_list = JSONEncoder(messages)

    return flask.Response(
        response=json.dumps(msg_list),
        mimetype="application/json",
    )


@app.route('/api/md5/<md5>')
@app.route('/api/md5sum/<md5>')
def api_md5sum(md5):
    messages = sm.File.by_md5(session, md5)
    msg_list = JSONEncoder(messages)

    return flask.Response(
        response=json.dumps(msg_list),
        mimetype="application/json",
    )


@app.route('/api/sha256/<sha256>')
@app.route('/api/sha256sum/<sha256>')
def api_sha256sum(sha256):
    messages = sm.File.by_sha256(session, sha256)
    msg_list = JSONEncoder(messages)

    return flask.Response(
        response=json.dumps(msg_list),
        mimetype="application/json",
    )


@app.route('/api/tar_sum/<tar_sum>')
def api_tar_sum(tar_sum):
    messages = sm.File.by_tar_sum(session, tar_sum)
    msg_list = JSONEncoder(messages)

    return flask.Response(
        response=json.dumps(msg_list),
        mimetype="application/json",
    )


# request files by tarball
@app.route('/api/tarball/<tarball>/filenames')
def api_tarball_filenames(tarball):
    # returns a list of tuples
    filenames = sm.File.tarball_filenames(session, tarball)

    # [0] to get the first element of tuple i.e. filename
    # [1:] to remove '/' from filename 0th position
    # This will allow querying by filename and get file data
    filename_list = [filename[0][1:] for filename in filenames]

    return flask.Response(
        response=json.dumps(filename_list),
        mimetype="application/json",
    )


@app.route('/api/package/<package>/filenames')
def api_package_filenames(package):
    # returns a list of tuples
    filenames = sm.File.package_filenames(session, package)

    # [0] to get the first element of tuple i.e. filename
    # [1:] to remove '/' from filename 0th position
    # This will allow querying by filename and get file data
    filename_list = [filename[0][1:] for filename in filenames]

    return flask.Response(
        response=json.dumps(filename_list),
        mimetype="application/json",
    )


@app.route('/api/package/<package>')
def api_package(package):
    tarball_list = sm.File.package_tarball(session, package)

    tarball_list = [tarball[0] for tarball in tarball_list]

    return flask.Response(
        response=json.dumps(list(tarball_list)),
        mimetype="application/json",
    )


@app.route('/api/compare/package/difference')
def api_compare_package_difference():
    package = flask.request.args.getlist('package', None)
    messages_list = []
    for pkg in package:
        messages = sm.File.by_package(session, pkg)
        if messages:
            messages = to_dict(messages)
            messages_list.append(messages)

    # calculate uncommon sha256sum
    common_sha256 = set.intersection(*map(set, messages_list))

    # delete messages with common sha256sum
    for messages in messages_list:
        for sha256 in common_sha256:
            messages.pop(sha256, None)

    return flask.Response(
        response=json.dumps(messages_list),
        mimetype="application/json",
    )


@app.route('/api/compare/package/common')
def api_compare_package_common():
    package = flask.request.args.getlist('package', None)
    messages_list = []
    for pkg in package:
        messages = sm.File.by_package(session, pkg)
        if messages:
            messages = to_dict(messages)
            messages_list.append(messages)

    # calculate common sha256 sum in messages_list
    common_sha256 = set.intersection(*map(set, messages_list))

    # adding messages with common sha256
    results = []
    for messages in messages_list:
        result = {}
        for sha256 in common_sha256:
            result[sha256] = messages[sha256]
        results.append(result)

    return flask.Response(
        response=json.dumps(results),
        mimetype="application/json",
    )


@app.route('/api/compare/tarball/difference')
def api_compare_tarball_difference():
    tarballs = flask.request.args.getlist('tarball', None)
    messages_list = []
    for tarball in tarballs:
        messages = sm.File.by_tarball(session, tarball)
        if messages:
            messages = to_dict(messages)
            messages_list.append(messages)

    # calculate uncommon sha256sum
    common_sha256 = set.intersection(*map(set, messages_list))

    # delete messages with common sha256sum
    for messages in messages_list:
        for sha256 in common_sha256:
            messages.pop(sha256, None)

    return flask.Response(
        response=json.dumps(messages_list),
        mimetype="application/json",
    )


@app.route('/api/compare/tarball/common')
def api_compare_tarball_common():
    tarballs = flask.request.args.getlist('tarball', None)
    messages_list = []
    for tarball in tarballs:
        messages = sm.File.by_tarball(session, tarball)
        if messages:
            messages = to_dict(messages)
            messages_list.append(messages)

    # calculate common sha256 sum in messages_list
    common_sha256 = set.intersection(*map(set, messages_list))

    # adding messages with common sha256
    results = []
    for messages in messages_list:
        result = {}
        for sha256 in common_sha256:
            result[sha256] = messages[sha256]
        results.append(result)

    return flask.Response(
        response=json.dumps(results),
        mimetype="application/json",
    )
