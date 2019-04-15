#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/1316:44 

import requests
import json

a = ['rabbit@sql5-209','rabbit@sql5-210','rabbit@sql5-211']
def GetMqnodes():
    url = 'http://172.16.5.209:15672/api/nodes'
    r = requests.get(url, auth=("guest", "guest"), timeout=5)
    parsed = json.loads(r.content)

    for i in parsed:
        name = i.get('running')
        mem_used = i.get('mem_used')
        mem_total = i.get('mem_limit')

        disk =i.get('disk_free')
        print name,mem_total,mem_used,disk



if __name__ == "__main__":
    GetMqnodes()
