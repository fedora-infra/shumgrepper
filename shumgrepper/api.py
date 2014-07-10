import json
import flask

from forms import InputForm
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
    for  package in packages:
        package_list.append(package[0])

    return flask.Response(
        response=json.dumps(package_list),
        mimetype="application/json",
    )


@app.route('/api/sha1/<sha1>')
def api_sha1sum(sha1):
    messages = sm.File.by_sha1(session, sha1)
    #converts message into list of dict
    msg_list = JSONEncoder(messages)

    return flask.Response(
        response=json.dumps(msg_list),
        mimetype="application/json",
    )


@app.route('/api/md5/<md5>')
def api_md5sum(md5):
    messages = sm.File.by_md5(session, md5)
    msg_list = JSONEncoder(messages)

    return flask.Response(
        response=json.dumps(msg_list),
        mimetype="application/json",
    )


@app.route('/api/sha256/<sha256>')
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


# request files by tarsum
@app.route('/api/tar_file/<tar_file>/filenames')
def api_tar_file(tar_file):
    messages = sm.File.by_tar_file(session, tar_file)
    file_list = []
    for message in messages:
        file_list.append(message.filename)

    return flask.Response(
        response=json.dumps(file_list),
        mimetype="application/json",
    )


@app.route('/api/package/<package>/filenames')
def api_package_filenames(package):
    messages = sm.File.by_package(session, package)
    file_list = []
    for message in messages:
        file_list.append(message.filename)

    return flask.Response(
        response=json.dumps(file_list),
        mimetype="application/json",
    )


@app.route('/api/package/<package>')
def api_package(package):
    messages = sm.File.by_package(session, package)
    file_list = []
    for message in messages:
        file_list.append(message.tar_file)

    file_list = set(file_list)

    return flask.Response(
        response=json.dumps(list(file_list)),
        mimetype="application/json",
    )


@app.route('/api/compare/packages/difference')
def api_compare_package_uncommon():
    package = flask.request.args.getlist('packages', None)
    messages_list = []
    for pkg in package:
        messages = sm.File.by_package(session, pkg)
        if messages:
            messages = JSONEncoder(messages)
            messages_list.append(messages)
    uncommon_files_list = uncommon_files(messages_list)

    return flask.Response(
        response = json.dumps(uncommon_files_list),
        mimetype = "application/json",
    )


@app.route('/api/compare/package/common')
def api_compare_package_common():
    package = flask.request.args.getlist('packages', None)
    messages_list = []
    for pkg in package:
        messages = sm.File.by_package(session, pkg)
        if messages:
            messages = JSONEncoder(messages)
            messages_list.append(messages)
    common_files_list = common_files(messages_list)

    return flask.Response(
        response = json.dumps(common_files_list),
        mimetype = "application/json",
    )


@app.route('/api/compare/difference')
def api_compare_difference():
    tar_files = flask.request.args.getlist('tar_file', None)
    messages_list = []
    for tar_file in tar_files:
        messages = sm.File.by_tar_file(session, tar_file)
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
        response = json.dumps(messages_list),
        mimetype = "application/json",
    )


@app.route('/api/compare/common')
def api_compare_common():
    tar_files = flask.request.args.getlist('tar_file', None)
    messages_list = []
    for tar_file in tar_files:
        messages = sm.File.by_tar_file(session, tar_file)
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
        response = json.dumps(results),
        mimetype = "application/json",
    )
