# -*- coding:utf-8 -*-
import flask
import fedmsg
import fedmsg.meta

from forms import InputForm
import summershum.model as sm

from shumgrepper.util import (
    JSONEncoder,
    uncommon_files,
    common_files,
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


#compare and return filenames uncommon in packages
@app.route('/compare/package', methods = ['GET', 'POST'])
@app.route('/compare/package/uncommon', methods = ['GET', 'POST'])
def compare_package_uncommon():
    form = InputForm(flask.request.form)

    if flask.request.method == "POST" and form.is_submitted():
        packages = form.values.data.split(',')
        messages_list = []
        for package in packages:
            messages = sm.File.by_package(session, package)
            if messages:
                messages = JSONEncoder(messages)
                messages_list.append(messages)
        uncommon_files_list = uncommon_files(messages_list)

        return flask.render_template(
            'compare.html',
            all_files = uncommon_files_list,
            compared_values = packages,
            length = len(packages),
        )
    return flask.render_template(
        'input_package.html',
        form = form,
    )


#compare and return filenames common in packages
@app.route('/compare/package/common', methods = ['GET', 'POST'])
def compare_package_common():
    form = InputForm(flask.request.form)

    if flask.request.method == "POST" and form.is_submitted():
        packages = form.values.data.split(',')
        messages_list = []
        for package in packages:
            messages = sm.File.by_package(session, package)
            if messages:
                messages = JSONEncoder(messages)
                messages_list.append(messages)
        common_files_list = common_files(messages_list)
        print common_files_list
        return flask.render_template(
            'compare.html',
            all_files = common_files_list,
            compared_values = packages,
            length = len(packages),
        )
    return flask.render_template(
        'input_package.html',
        form = form,
    )


#compare and return filenames uncommon in tar_files
@app.route('/compare/tar_file', methods = ['GET', 'POST'])
@app.route('/compare/tar_file/uncommon', methods = ['GET', 'POST'])
def compare_tar_file_uncommon():
    form = InputForm(flask.request.form)

    if flask.request.method == "POST" and form.is_submitted():
        tar_files = form.values.data.split(',')
        messages_list = []
        for tar_file in tar_files:
            messages = sm.File.by_tar_file(session, tar_file)
            if messages:
                messages = JSONEncoder(messages)
                messages_list.append(messages)
        uncommon_files_list = uncommon_files(messages_list)

        return flask.render_template(
            'compare.html',
            all_files = uncommon_files_list,
            compared_values = tar_files,
            length = len(tar_files),
        )
    return flask.render_template(
        'input_tar_file.html',
        form = form,
    )


#compare and return filenames common in tar_files
@app.route('/compare/tar_file', methods = ['GET', 'POST'])
@app.route('/compare/tar_file/common', methods = ['GET', 'POST'])
def compare_tar_file_common():
    form = InputForm(flask.request.form)

    if flask.request.method == "POST" and form.is_submitted():
        tar_files = form.values.data.split(',')
        messages_list = []
        for tar_file in tar_files:
            messages = sm.File.by_tar_file(session, tar_file)
            if messages:
                messages = JSONEncoder(messages)
                messages_list.append(messages)
        common_files_list = common_files(messages_list)

        return flask.render_template(
            'compare.html',
            all_files = common_files_list,
            compared_values = tar_files,
            length = len(tar_files),
        )
    return flask.render_template(
        'input_tar_file.html',
        form = form,
    )
