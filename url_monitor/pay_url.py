#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/412:22 
import requests
import time
import sys
import  datetime


class url_m(object):
    def __init__(self,url):
        self.url = url

    def url_status(self):
        req = requests.get(self.url)
        return req.status_code

    def url_time(self):  #毫秒
        start_time = datetime.datetime.now()
        req = requests.get(self.url)
        now_time = (datetime.datetime.now()-start_time).microseconds/1000
        return now_time

    def test(self):
        print "this URL_TIMR IS: %s " % self.url_time()
        print "this URL_STATS IS: %s" % self.url_status()


def check_url(kind, url):
    URL = url_m(url)
    if kind == 'status':
        print URL.url_status()
    elif kind == 'time':
        print URL.url_time()
    else:
         URL.test()


if __name__ == "__main__":
    kind = sys.argv[1]
    url = sys.argv[2]
    check_url(kind, url)
