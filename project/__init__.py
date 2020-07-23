__version__ = '0.1'

from flask import Flask
#from flask.ext.scss import Scss

app = Flask('project')
app.config['SECRET_KEY'] ='random'

#Scss(app, static_dir='static', asset_dir='assets')

import project.model
import project.controller
