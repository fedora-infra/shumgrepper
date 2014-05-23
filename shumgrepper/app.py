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

@app.route('/summershum/')
@app.route('/summershum')
def summershum():
    sha1sum = flask.request.args.get('sha1sum', None)
    if sha1sum:
        message = sm.File.by_sha1(session, sha1sum)

    md5sum = flask.request.args.get('md5sum', None)
    if md5sum:
        message = sm.File.by_md5(session, md5sum)

    print message

