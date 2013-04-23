#!/usr/bin/env python

"""
urllib2 examples from Python How-To
"""

import urllib
import urllib2
import SimpleHTTPServer

def encode():
    url = 'http://www.cgi101.com/book/ch20/login2.cgi'
    values = {'username' : 'Michael Foord',
              'password' : 'Northampton',
              'language' : 'Python' }

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent' : user_agent}

    data = urllib.urlencode(values)

    #if no data is passed, GET will be used (POST with data)
    req = urllib2.Request(url, data, headers)
    try:
        response = urllib2.urlopen(req)
        the_page = response.read()
        print the_page
    except IOError as merr:
        print "error: {0}".format(merr)

if __name__ == '__main__':
    encode()

    for key,val in SimpleHTTPServer.BaseHTTPServer.BaseHTTPRequestHandler.responses.iteritems():
        print "{0} {1}".format(key, val)
