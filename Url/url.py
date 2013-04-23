#!/usr/bin/env python

"""
URL examples
"""

import urllib2

def print_response(response):
    """Print response from urlopen"""
    if not response:
        return

    print "response.url: {0}".format(response.geturl())
    #meta-information of the page (headers, 
    print "response.info: {0}".format(response.info())
    #HTTP response code
    print "response.code: {0}".format(response.getcode())
    #print 100 bytes from response
    print "response[100]: {0}".format(response.read(100))
    #print  response
    #print "response: {0}".format(response.read())
    print '-'*50

def open_url(url):
    """Open URL"""
    try:
        #urlopen(url, [data], [timeout]
        response = urllib2.urlopen(url, None, 5)
        print_response(response)

    except urllib2.URLError as urlerr:
        print "Invalid URL: {0} error: {1}".format(url, urlerr.strerror)

def add_headers():
    """Add some headers"""
    req = urllib2.Request('http://www.example.com/')
    req.add_header('Referer', 'http://www.python.org/')
    req.add_header('User-agent', 'Mozilla/5.0')
    r = urllib2.urlopen(req)
    print_response(r)

def use_opener():
    """Use OpenerDirector"""
    #return an OpenerDirector instance
    opener = urllib2.build_opener()
    #add header
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #open
    response = opener.open('http://www.example.com/')
    print_response(response)

if __name__ == '__main__':
    open_url("http://www.google.com")

    add_headers()

    use_opener()
