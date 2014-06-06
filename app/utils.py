import urllib2

LOREM_IPSUM_ME_URL = 'http://lorem-ipsum.me/api/text'

def get_filler():
    """Return filler text."""
    filler = urllib2.urlopen(LOREM_IPSUM_ME_URL).read()
    return filler
