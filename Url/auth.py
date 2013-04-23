#!/usr/bin/env python

"""
Basic authentication:
- client makes a request to a webpage
- server responds with error, requesting authentication
- client retries request, with authentication details encoded in request
- server checks details, sends the requested page or another error
"""

import urllib2
import sys
import getpass
import socket

def test_get_page():
    theurl = 'http://test.webdav.org/auth-basic/'
    req = urllib2.Request(theurl)
    try:
         handle = urllib2.urlopen(req)
         print handle.getcode()
    except IOError, e:
         if hasattr(e, 'code'):
             if e.code != 401:
                 print 'We got another error'
                 print e.code
             else:
                 #401 means "Not authenticated"
                 print "Error; Not authenticated!!!"
                 print e.headers
                 print e.headers['www-authenticate']

def get_page(user, password):
    """Authenticates on a realm"""

    #set default timeout
    socket.setdefaulttimeout(2)

    url =  'http://test.webdav.org/auth-basic/'
    #create a password manager
    #Keep a DB of (realm, uri) -> (user, passwd); if None --> catch-all realm
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()

    #add_password(realm, uri, user, password):
    #(user,pswd) will be used to authenticate for realm and super-uri of uri
    passman.add_password(None, url, user, password)
    # because we have put None at the start it will always
    # use this username/password combination for  urls
    # for which `url` is a super-url

    #create AuthHandler
    #will handle authentication to remote host
    authhandler = urllib2.HTTPBasicAuthHandler(passman)

    #returns an OpenerDirector instance, which chains the handlers in given order
    opener = urllib2.build_opener(authhandler)

    urllib2.install_opener(opener)
    # All calls to urllib2.urlopen will now use our handler
    # Make sure not to include the protocol in with the URL, or
    # HTTPPasswordMgrWithDefaultRealm will be very confused.
    # You must (of course) use it when fetching the page though.

    try:
        pagehandle = urllib2.urlopen(url)
    except urllib2.URLError as ioerr:
        #if hasattr(ioerr, 'reason'):
        #    print "Failed to reach a server; reason: {0}".format(ioerr.reason)
        #    sys.exit(2)

        if hasattr(ioerr, 'code'):
            if ioerr.code != 401:
                print "error: {0}".format(ioerr)
            else:
                print "Auth failed, will exit: {0}".format(ioerr)
                sys.exit(1)
        else:
            print "Failed to reach a server; reason: {0}".format(ioerr.reason)
            sys.exit(2)

    print "Authentication succeeded!!!"


if __name__ == '__main__':
    #test_get_page()
    user = "user1"
    #password = "user1"
    password = getpass.getpass()
    get_page(user, password)
