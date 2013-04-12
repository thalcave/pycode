#!/usr/bin/env python
import urllib2
import cookielib
import getpass
from datetime import date
from urllib import urlencode

class Filler:
    def __init__(self, user, password):
        self.browser = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.LWPCookieJar()))
        login_response = self.browser.open(self.browser.open("http://timsato.tool.1and1.com/xml/enter/effort").geturl(),
                                           urlencode({"__username": user,
                                                      "__password": password,
                                                      "submit": " Login "}))
        self.url = login_response.geturl()
        if self.url.startswith('https://login.intranet.1and1.com/'):
            raise Exception("Login failed")

    def work(self, day):
        date_t = (day.day, day.month, day.year)
        self.browser.open(self.url, urlencode({"__from": "%02d.%02d.%d" % date_t}))
        enter_effort = self.browser.open(self.url,
                                         urlencode({"__from": "%02d.%02d.%d" % date_t,
                                                    "__handler": "handler.enter/effort.effortenterhandler#%02d%02d%d" % date_t,
                                                    "usage": "",
                                                    "start_time": "10",
                                                    "end_time": "18",
                                                    "duration": "8",
                                                    "project": "TEC.1246",
                                                    "task": "dev",
                                                    "comment": "auto",
                                                    }))

    def workdays(self, begin, end):
        for o in range(begin.toordinal(), end.toordinal() + 1):
            day = date.fromordinal(o)
            if day.isoweekday() <= 5:
                print day
                self.work(day)

password = getpass.getpass()
f = Filler("fmicu", password)
f.workdays(date(2010, 5, 10), date.today())
