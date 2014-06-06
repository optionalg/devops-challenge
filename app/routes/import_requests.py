from flask import Blueprint

from app import app
from app.utils import get_filler

import_requests = Blueprint('import_requests', __name__)


@import_requests.route('/import-requests')
def do_import_requests():
    """Import the requests module."""
    app.logger.info(get_filler())
    import requests
    return "Requests module imported successfully"
