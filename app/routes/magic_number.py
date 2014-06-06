import random
import time
import sys

from flask import Blueprint, request

from app import app
from app.utils import get_filler

MAX_INT = 100000000000
TIMESTAMP_MODULO = 5

magic_number = Blueprint('magic_number', __name__)

def shutdown_server():
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func:  # Running with the Werkzeug Server
        shutdown_func()
    else:
        sys.exit(1)

@magic_number.route('/magic-number')
def get_magic_number():
    """Return a magic number."""
    app.logger.info(get_filler())
    random_integer = random.randint(1, MAX_INT)
    timestamp = int(time.time())
    try:
        magic_number = random_integer / (timestamp % TIMESTAMP_MODULO)
    except ZeroDivisionError:
        magic_number = 0
        shutdown_server()
    return str(magic_number)
