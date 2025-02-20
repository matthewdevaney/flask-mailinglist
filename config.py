import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # auto reload pages during development when changes are made
    TEMPLATES_AUTO_RELOAD = True

    # wtforms
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'