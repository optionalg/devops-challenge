#! /usr/bin/env python

###
### This main.py file is the entry point for the http server app, even if not
### running directly by executing this file as __main__.  Routes should be
### registered on the app here.
###

from app import app
from app.routes.current_time import current_time
from app.routes.import_requests import import_requests
from app.routes.magic_number import magic_number
from app.routes.venmo_logo import venmo_logo

app.register_blueprint(current_time)
app.register_blueprint(import_requests)
app.register_blueprint(magic_number)
app.register_blueprint(venmo_logo)


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
