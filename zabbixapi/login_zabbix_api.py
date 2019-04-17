#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/4/1710:10 

import urllib2
import json
url = "http://106.14.171.112:8080/zabbix/api_jsonrpc.php"
username = 'admin'
password = 'zabbix'

def requestJson(url,values):
    data = json.dumps(values)
    req = urllib2.Request(url, data, {'Content-Type': 'application/json-rpc'})
    response = urllib2.urlopen(req, data)
    output = json.loads(response.read())
    print output
    try:
        message = output['result']
    except:
        message = output['error']['data']
        print message
        quit()

    return output['result']

#API接口认证的函数，登录成功会返回一个Token
def authenticate(url, username, password):
    values = {'jsonrpc': '2.0',
              'method': 'user.login',
              'params': {
                  'user': username,
                  'password': password
              },
              'id': '0'
              }
    idvalue = requestJson(url,values)
    return idvalue

auth =authenticate(url, username,password)