# -*- coding:utf-8 -*-
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

def modify_rst(rst):
    """ Downgrade some of our rst directives if docutils is too old. """

    try:
        # The rst features we need were introduced in this version
        minimum = [0, 9]
        version = map(int, docutils.__version__.split('.'))

        # If we're at or later than that version, no need to downgrade
        if version >= minimum:
            return rst
    except Exception:
        # If there was some error parsing or comparing versions, run the
        # substitutions just to be safe.
        pass

    # Otherwise, make code-blocks into just literal blocks.
    substitutions = {
        '.. code-block:: javascript': '::',
    }
    for old, new in substitutions.items():
        rst = rst.replace(old, new)

    return rst

def modify_html(html):
    """ Perform style substitutions where docutils doesn't do what we want.
    """

    substitutions = {
        '<tt class="docutils literal">': '<code>',
        '</tt>': '</code>',
    }
    for old, new in substitutions.items():
        html = html.replace(old, new)

    return html

def preload_docs(endpoint):
    """ Utility to load an RST file and turn it into fancy HTML. """

    here = os.path.dirname(os.path.abspath(__file__))
    fname = os.path.join(here, 'docs', endpoint + '.rst')
    with codecs.open(fname, 'r', 'utf-8') as f:
        rst = f.read()

    rst = modify_rst(rst)

    api_docs = docutils.examples.html_body(rst)

    api_docs = modify_html(api_docs)

    api_docs = markupsafe.Markup(api_docs)
    return api_docs

htmldocs = dict.fromkeys(['query_api'])
for key in htmldocs:
    htmldocs[key] = preload_docs(key)

def load_docs(request):
    URL = app.config.get('SHUMGREPPER_BASE_URL', request.url_root)
    docs = htmldocs[request.endpoint]
    docs = jinja2.Template(docs).render(URL=URL)
    return markupsafe.Markup(docs)

@app.route('/query_api')
def query_api():
    return flask.render_template(
        'query_api.html',
        docs=load_docs(flask.request)
    )


@app.route('/')
def home():
    return flask.render_template('home.html')


# list the names of packages
@app.route('/packages')
def packages():
    packages = sm.File.packages(session)
    package_list = []
    for  package in packages:
        package_list.append(package[0])

    return flask.render_template(
        'packages.html',
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
@app.route('/tar/<tar>')
def tar_sum(tar):
    messages = sm.File.by_tar_sum(session, tar)
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
    print file_list
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
@app.route('/compare/packages', methods = ['GET', 'POST'])
@app.route('/compare/packages/uncommon', methods = ['GET', 'POST'])
def compare_uncommon():
    form = InputForm(flask.request.form)

    if flask.request.method == "POST" and form.is_submitted():
        packages = form.package.data.split(',')
        messages_list = []
        for package in packages:
            messages = sm.File.by_package(session, package)
            if messages:
                messages = JSONEncoder(messages)
                messages_list.append(messages)
        uncommon_files_list = uncommon_files(messages_list)

        return flask.render_template(
            'compare_packages.html',
            all_files = uncommon_files_list,
            packages = packages,
            length = len(packages),
        )
    return flask.render_template(
        'input.html',
        form = form,
    )


#compare and return filenames common in packages
@app.route('/compare/packages/common', methods = ['GET', 'POST'])
def compare_common():
    form = InputForm(flask.request.form)

    if flask.request.method == "POST" and form.is_submitted():
        packages = form.package.data.split(',')
        messages_list = []
        for package in packages:
            messages = sm.File.by_package(session, package)
            if messages:
                messages = JSONEncoder(messages)
                messages_list.append(messages)
        common_files_list = common_files(messages_list)

        return flask.render_template(
            'compare_packages.html',
            all_files = common_files_list,
            packages = packages,
            length = len(packages),
        )
    return flask.render_template(
        'input.html',
        form = form,
    )
