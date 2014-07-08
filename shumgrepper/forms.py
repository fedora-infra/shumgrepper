from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class InputForm(Form):
    values = TextField('values', validators = [Required()])
