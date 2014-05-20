import json
import flask
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy

from bunch import Bunch
import codecs
import docutils
import docutils.examples
import dogpile.cache
from functools import wraps
import jinja2
import markupsafe
import os
import time
import traceback

import pygments
import pygments.lexers
import pygments.formatters

from datetime import datetime
import fedmsg
import fedmsg.meta
import fedmsg.config

import summershum.model as sm
import summershum.cli as sc

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

