#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/1514:18 

import requests
import sys
import json
def get_url_infomation(storecode,chl):
    url = "http://172.16.4.102:9083/misc.service/s?code=%s&channel=%s" % (storecode,chl)
    result = requests.get(url)
    print json.loads(result.content)

if __name__ == "__main__":
    storecode = sys.argv[1]
    chl = sys.argv[2]
    get_url_infomation(storecode,chl)
