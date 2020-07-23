#!/usr/bin/env python

from project import app
from project.model import evaluate

if __name__=='__main__':
    app.run('0.0.0.0',debug=True)