#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/423:38 

from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import DescribeResourceUsageRequest,DescribeDBInstancePerformanceRequest
import json,sys,datetime


AcesskeyID = 'LTAIk1fHVSSahLxN'
AcesskeySecret = 'usd1W47lTFXhhTIR5Cq5WTw9M3qACg'
regionid = 'cn-hangzhou'
clt = client.AcsClient(
    AcesskeyID,
    AcesskeySecret,
    regionid)

def GetResource(kinds):
        ResourceUsage = DescribeResourceUsageRequest.DescribeResourceUsageRequest()
        ResourceUsage.set_accept_format('json')
        ResourceUsage.set_DBInstanceId('rm-bp18144qkyj20731o')
        ResourceUsageInfo = clt.do_action_with_exception(ResourceUsage)
        print ResourceUsageInfo
        Info = (json.loads(ResourceUsageInfo))[kinds]

        return Info

def test(kinds):
    if(kinds == "SQLSize"):
        GetResource(kinds)
    elif(kinds == "Engine"):
        GetResource(kinds)
    if (kinds == "DiskUsed"):
        GetResource(kinds)
    elif (kinds == "BackupOssDataSize"):
        GetResource(kinds)
    if(kinds == "DBInstanceId"):
        GetResource(kinds)
    elif(kinds == "LogSize"):
        GetResource(kinds)
    if (kinds == "BackupSize"):
        GetResource(kinds)
    elif (kinds == "BackupOssLogSize"):
        GetResource(kinds)
    if (kinds == "ColdBackupSize"):
        GetResource(kinds)
    elif (kinds == "DataSize"):
        GetResource(kinds)
if __name__ == "__main__":
    kinds = sys.argv[1]
    test1 = GetResource(kinds)
    print test1
