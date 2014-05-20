import os

if not os.environ.get("SHUMGREPPER_CONFIG"):
    os.environ["SHUMGREPPER_CONFIG"] = '../development.cfg'

from shumgrepper.app import db
db.create_all()
