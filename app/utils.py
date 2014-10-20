import urllib2

LOREM_IPSUM_URL = 'http://loripsum.net/api/plaintext'

def get_filler():
    """Return filler text."""
    filler = urllib2.urlopen(LOREM_IPSUM_URL).read()
    return filler
