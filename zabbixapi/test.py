#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/2721:04 

import json
import urllib2

url = "http://106.14.171.112:8080/zabbix/api_jsonrpc.php"
header = {"Content-Type": "application/json"}

data = json.dumps(
{
   "jsonrpc": "2.0",
   "method": "user.login",
   "params": {
   "user": "admin",
   "password": "zabbix"
},
"id": 0
})
# create request object
request = urllib2.Request(url, data)
for key in header:
   request.add_header(key,header[key])
try:
   result = urllib2.urlopen(request)
except urllib2.URLError as e:
   print "Auth Failed, Please Check Your Name AndPassword:", e.reason
else:
    response = json.loads(result.read())
    result.close()
    print"Auth Successful. The Auth ID Is:", response['result']
