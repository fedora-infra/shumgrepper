import json
import flask
import fedmsg
import fedmsg.meta

from forms import InputForm
import summershum.model as sm

from shumgrepper.util import (
    request_wants_html,
    JSONEncoder,
)

app = flask.Flask(__name__)

fedmsg_config = fedmsg.config.load_config()
fedmsg.meta.make_processors(**fedmsg_config)

session = sm.create_session(
    fedmsg_config['summershum.sqlalchemy.url'],
    create=True,
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
    form = InputForm(flask.request.form)

    if flask.request.method == "POST" and form.is_submitted():
        package_list = form.package.data.split(',')
        final_list = []

        for a_package in package_list:
            message = sm.File.by_package(session, a_package)
            if message:
                sha1sum_list = []
                for msg in message:
                    sha1sum_list.append(msg.sha1sum)
                final_list.append(sha1sum_list)

        common_list = set(final_list[0]).intersection(*final_list)

        common_filenames = []
        for sha1sum in common_list:
            for msg in message:
                if sha1sum == msg.sha1sum:
                    common_filenames.append(msg.filename)

        return flask.render_template(
            'same_files.html',
            all_files = common_filenames, 
            count=len(common_filenames),
            package_list = package_list,
        )
    return flask.render_template(
            'input.html',
            form = form
    )

