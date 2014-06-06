devops-challenge
================

This Flask app provides these endpoints:

* /current-time - Returns the current time
* /import-requests - Imports the [requests](http://docs.python-requests.org/ "Title") module
* /magic-number - Returns a magic number
* /venmo-logo - Returns the Venmo logo

Some of these are broken in the following ways:

* /current-time - Makes a blocking call
* /magic-number - Occasionally crashes the app
