from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class InputForm(Form):
    package = TextField('package', validators = [Required()])
