import flask
import fedmsg
import fedmsg.meta

import summershum.model as sm

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

    return flask.render_template('files.html', all_files=message)


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

