#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/2515:29 
#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/1316:44

import requests
import json
import sys
def GetMqStatus(node):
    url = 'http://172.16.5.209:15672/api/nodes/%s'  % node
    r = requests.get(url, auth=("guest", "guest"), timeout=5)
    parsed = json.loads(r.content)
    status = parsed.get('running')
    return status

# def decide_node(node):
#     nodename = GetMqnodes(node)
#     if node == nodename:
#          print node
#     else:
#          print "you input rabbitmq nodename is error"

if __name__ == "__main__":
    node = sys.argv[1]
    status = GetMqStatus(node)
    if status == True:
        print 1
    else:
        print 0

