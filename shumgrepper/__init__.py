# -*- coding:utf-8 -*-
import flask
import fedmsg
import fedmsg.meta

from forms import InputForm
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


@app.route('/')
def home():
    return flask.render_template('home.html')


# list the names of packages
@app.route('/packages')
def list_all_packages():
    packages = sm.File.get_all_packages(session)
    package_list = []
    for  package in packages:
        package_list.append(package[0])

    return flask.render_template(
        'list_all_packages.html',
        packages = package_list
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
def tar_file(tar_file):
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
    messages = sm.File.by_package(session, package)
    file_list = []
    for message in messages:
        file_list.append(message.filename)

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


#compare and return filenames uncommon in tar_files
@app.route('/compare', methods = ['GET', 'POST'])
@app.route('/compare/difference', methods = ['GET', 'POST'])
def compare_difference():
    form = InputForm(flask.request.form)

    if flask.request.method == "POST" and form.is_submitted():
        tar_files = form.values.data.split(',')
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
    return flask.render_template(
        'input_tar_file.html',
        form = form,
    )


#compare and return filenames common in tar_files
@app.route('/compare/common', methods = ['GET', 'POST'])
def compare_common():
    form = InputForm(flask.request.form)

    if flask.request.method == "POST" and form.is_submitted():
        tar_files = form.values.data.split(',')
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
    return flask.render_template(
        'input_tar_file.html',
        form = form,
    )
