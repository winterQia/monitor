#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/4/1012:23 

import requests,json

url = "https://paas.365ops.cn/login"
headers = {'Content-Type':'application/json;charset=UTF-8'}
request_param = {
    "username": "admin",
    "password": "P@ssw0rd123"
}
response = requests.post(url, data=json.dumps(request_param), headers=headers, verify=False)

print response.text, response.status_code