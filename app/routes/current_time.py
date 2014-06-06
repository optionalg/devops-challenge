import socket
import struct
import time

from flask import Blueprint

from app import app
from app.utils import get_filler

SOCKET_TIMEOUT = 10
# The first host on this will purposely cause a timeout
TIME_HOSTS = ('time-nist.symmetricom.com', 'time-c.nist.gov')
TIME_PORT = 37
# reference time (in seconds since 1900-01-01 00:00:00)
TIME_1970 = 2208988800

current_time = Blueprint('current_time', __name__)


@current_time.route('/current-time')
def get_current_time():
    """Return the current time."""
    app.logger.info(get_filler())
    # Try each host until one succeeds
    for host in TIME_HOSTS:
        time_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time_socket.settimeout(SOCKET_TIMEOUT)
        try:
            time_socket.connect((host, TIME_PORT))
        except Exception:
            pass
        else:
            output = time_socket.recv(4)
            time_socket.close()

            elapsed_seconds = struct.unpack("!I", output)[0]
            epoch_seconds = int(elapsed_seconds - TIME_1970)
            return time.ctime(epoch_seconds)
    else:
        return "Couldn't get current time"
