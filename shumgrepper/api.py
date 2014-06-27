import json
import flask
import os
import codecs
import jinja2
import docutils
import docutils.examples
import markupsafe
import fedmsg
import fedmsg.meta

from forms import InputForm
import summershum.model as sm

from shumgrepper import app, session

from shumgrepper.util import (
    JSONEncoder,
    uncommon_files,
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


@app.route('/api/tar/<tar>')
def api_tar_sum(tar):
    messages = sm.File.by_tar_sum(session, tar)
    msg_list = JSONEncoder(messages)

    return flask.Response(
        response=json.dumps(msg_list),
        mimetype="application/json",
    )


@app.route('/api/package/<package>/filenames')
def api_package(package):
    messages = sm.File.by_package(session, package)
    file_list = []
    for message in messages:
        file_list.append(message.filename)

    return flask.Response(
        response=json.dumps(file_list),
        mimetype="application/json",
    )


@app.route('/api/compare')
def api_compare():
    packages = flask.request.args.getlist('packages', None)
    messages_list = []
    for package in packages:
        messages = sm.File.by_package(session, package)
        if messages:
            messages = JSONEncoder(messages)
            messages_list.append(messages)
    uncommon_files_list = uncommon_files(messages_list)

    return flask.Response(
        response = json.dumps(uncommon_files_list),
        mimetype = "application/json",
    )

