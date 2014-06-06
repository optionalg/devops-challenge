import os

from flask import Blueprint, send_file

from app import app
from app.utils import get_filler

VENMO_LOGO_PATH = os.path.join(app.config['STATIC_DIR'], 'venmo-logo-blue.png')

venmo_logo = Blueprint('venmo_logo', __name__)


@venmo_logo.route('/venmo-logo')
def get_venmo_logo():
    """Return the Venmo logo."""
    app.logger.info(get_filler())
    return send_file(VENMO_LOGO_PATH)
