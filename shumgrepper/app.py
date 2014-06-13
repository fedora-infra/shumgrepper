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
@app.route('/sha1/<sha1>')
def sha1sum(sha1):
    message = sm.File.by_sha1(session, sha1)
    mimetype = flask.request.headers.get('Accept')
    #converts message into list of dict
    msg_list = JSONEncoder(message)

    if mimetype == '*/*':
        mimetype = 'application/json'

    if request_wants_html():
        return flask.render_template(
            'files.html',
            all_files=msg_list
        )
    else:
        message_json = json.dumps(msg_list)
        return flask.Response(
            response=message_json,
            mimetype=mimetype,
        )


# request files by md5sum
@app.route('/md5/<md5>')
@app.route('/md5/<md5>')
def md5sum(md5):
    message = sm.File.by_md5(session, md5)

    return flask.render_template('files.html', all_files=message)


# request files by sha256sum
@app.route('/sha256/<sha256>')
@app.route('/sha256/<sha256>')
def sha256sum(sha256):
    message = sm.File.by_sha256(session, sha256)

    return flask.render_template('files.html', all_files=message)


# request files by tarsum
@app.route('/tar/<tar>')
@app.route('/tar/<tar>')
def tar_sum(tar):
    message = sm.File.by_tar_sum(session, tar)

    return flask.render_template('files.html', all_files=message)

# list filenames present in a package
@app.route('/package/<package>/filenames')
def package(package):
    message = sm.File.by_package(session, package)

    return flask.render_template('filename.html', all_files=message, argument=package, count=len(message))


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

