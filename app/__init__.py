""" Initialize & configure the Flask app object

    Doing this here ensures that anytime we access the app object it has
    already been configured.
"""

from flask import Flask

###
### Flask
###
app = Flask('devops-challenge')
app.config.from_object('app.settings')


###
### Other configuration that must happen at app load goes here...
###
