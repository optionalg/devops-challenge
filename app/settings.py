""" Basic flask settings, if blocks to designate environment.

    Runnable code (rather than just configuration definitions) such as
    initializing libraries should just live in app/__init__.py (or in its own
    file if it gets too complex, but imported by app/__init__.py)
"""
import os
import sys
import logging

FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'

###
### Defaults
DEBUG = False
STATIC_DIR = os.path.abspath('app/static')

###
### By environment
if FLASK_ENV == 'development':
    DEBUG = True

if FLASK_ENV == 'testing':
    # In tests, send everything to stdout which we can capture as necessary
    logging.basicConfig(stream=sys.stdout)
