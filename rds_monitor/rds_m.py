#!/usr/bin/python
# encoding=utf-8


from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import DescribeRegionsRequest
import json

AcesskeyID = 'LTAIk1fHVSSahLxN'
AcesskeySecret = 'usd1W47lTFXhhTIR5Cq5WTw9M3qACg'
regionid = 'cn-hangzhou'
clit = client.AcsClient(
    AcesskeyID,
    AcesskeySecret,
    regionid)

request = DescribeRegionsRequest.DescribeRegionsRequest()
request.set_accept_format('json')
request.set_action_name('DescribeDBInstancePerformance')
# 多个性能指标用 "," 分隔
request.set_query_params(
    dict(DBInstanceId="数据库实例名", key="性能指标"))
print clit.do_action_with_exception(request)
