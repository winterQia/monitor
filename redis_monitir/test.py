#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/312:18
# import redis
# def login_redis():
#     host = '172.16.4.99'
#     prot = 6379
#     rds = redis.StrictRedis('172.16.4.99',6379)
#     try:
#         info = rds.info()
#         print info
#     except Exception, e:
#         print 1
# login_redis()

import subprocess
cmd = 'nc -z %s %s > /dev/null 2>&1' % ('192.168.200.174', 6379)
print subprocess.call(cmd, shell=True)