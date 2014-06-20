import json
import flask
import fedmsg
import fedmsg.meta

from forms import InputForm
import summershum.model as sm

from shumgrepper.util import (
    request_wants_html,
    JSONEncoder,
    common_files,
)

app = flask.Flask(__name__)

fedmsg_config = fedmsg.config.load_config()
fedmsg.meta.make_processors(**fedmsg_config)

session = sm.create_session(
    fedmsg_config['summershum.sqlalchemy.url'],
    create=True,
    )

@app.route('/')
def home():
    return flask.render_template('home.html')


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
    #converts message into list of dict
    msg_list = JSONEncoder(messages)
    mimetype = flask.request.headers.get('Accept')
    if mimetype == '*/*':
        mimetype = 'application/json'

    if request_wants_html():
        return flask.render_template(
            'files.html',
            all_files=msg_list
        )
    else:
        return flask.Response(
            response=json.dumps(msg_list),
            mimetype=mimetype,
        )


# request files by md5sum
@app.route('/md5/<md5>')
def md5sum(md5):
    messages = sm.File.by_md5(session, md5)
    msg_list = JSONEncoder(messages)

    mimetype = flask.request.headers.get('Accept')
    if mimetype == '*/*':
        mimetype = 'application/json'

    if request_wants_html():
        return flask.render_template(
            'files.html',
            all_files=msg_list
        )
    else:
        return flask.Response(
            response=json.dumps(msg_list),
            mimetype=mimetype,
        )


# request files by sha256sum
@app.route('/sha256/<sha256>')
def sha256sum(sha256):
    messages = sm.File.by_sha256(session, sha256)
    msg_list = JSONEncoder(messages)

    mimetype = flask.request.headers.get('Accept')
    if mimetype == '*/*':
        mimetype = 'application/json'

    if request_wants_html():
        return flask.render_template(
            'files.html',
            all_files=msg_list
        )
    else:
        return flask.Response(
            response=json.dumps(msg_list),
            mimetype=mimetype,
        )


# request files by tarsum
@app.route('/tar/<tar>')
def tar_sum(tar):
    messages = sm.File.by_tar_sum(session, tar)
    msg_list = JSONEncoder(messages)

    mimetype = flask.request.headers.get('Accept')
    if mimetype == '*/*':
        mimetype = 'application/json'

    if request_wants_html():
        return flask.render_template(
            'files.html',
            all_files=msg_list
        )
    else:
        return flask.Response(
            response=json.dumps(msg_list),
            mimetype=mimetype,
        )


# list filenames present in a package
@app.route('/package/<package>/filenames')
def package(package):
    messages = sm.File.by_package(session, package)
    file_list = []
    for message in messages:
        file_list.append(message.filename)

    mimetype = flask.request.headers.get('Accept')
    if mimetype == '*/*':
        mimetype = 'application/json'

    if request_wants_html():
        return flask.render_template(
            'filename.html',
            all_files=file_list,
            count=len(file_list),
        )
    else:
        return flask.Response(
            response=json.dumps(file_list),
            mimetype=mimetype,
        )


#compare and return filenames common in packages
@app.route('/compare', methods = ['GET', 'POST'])
def compare():

    mimetype = flask.request.headers.get('Accept')

    if mimetype == '*/*':
        mimetype = 'application/json'

    if request_wants_html():
        form = InputForm(flask.request.form)

        if flask.request.method == "POST" and form.is_submitted():
            packages = form.package.data.split(',')
            messages_list = []
            for package in packages:
                messages = sm.File.by_package(session, package)
                if messages:
                    messages_list.append(messages)
            common_filenames = common_files(messages_list)
            return flask.render_template(
                'filename.html',
                all_files = common_filenames,
                count=len(common_filenames),
            )
        return flask.render_template(
            'input.html',
            form = form,
        )
    else:
        packages = flask.request.args.getlist('packages', None)
        messages_list = []
        for package in packages:
            messages = sm.File.by_package(session, package)
            if messages:
                messages_list.append(messages)
        common_filenames = common_files(messages_list)

        return flask.Response(
            response = json.dumps(common_filenames),
            mimetype = mimetype,
        )

