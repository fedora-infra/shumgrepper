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

# list filenames present in a package
@app.route('/package/<package>/filenames')
def package(package):
    message = sm.File.by_package(session, package)

    return flask.render_template('filename.html', all_files=message, argument=package, count=len(message))

@app.route('/package/compare/<package1>/<package2>')
def compare(package1, package2):
    message1 = sm.File.by_package(session, package1)
    message2 = sm.File.by_package(session, package2)

    filename1, filename2, same_files = {}, {}, []

    for msg in message1:
        filename1[msg.sha1sum] = msg.filename

    for msg in message2:
        filename2[msg.sha1sum] = msg.filename

    for key,value in filename1.iteritems():
        if key in filename2: 
            same_files.append(value) 

    return flask.render_template('same_files.html', all_files=same_files, argument1=package1, argument2=package2, count=len(same_files))

