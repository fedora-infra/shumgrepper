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

