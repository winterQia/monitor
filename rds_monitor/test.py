#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/114:55
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

# Type = sys.argv[1]
# DBInstanceId = sys.argv[2]
Key = sys.argv[1]

# 阿里云返回的数据为UTC时间，因此要转换为东八区时间。其他时区同理。
UTC_End = datetime.datetime.today() - datetime.timedelta(hours=8)
UTC_Start = UTC_End - datetime.timedelta(minutes=25)

StartTime = datetime.datetime.strftime(UTC_Start, '%Y-%m-%dT%H:%MZ')
EndTime = datetime.datetime.strftime(UTC_End, '%Y-%m-%dT%H:%MZ')

def GetPerformance(MasterKey,IndexNum,StartTime,EndTime):
    Performance = DescribeDBInstancePerformanceRequest.DescribeDBInstancePerformanceRequest()
    Performance.set_accept_format('json')
    Performance.set_DBInstanceId('rm-bp18144qkyj20731o')
    Performance.set_Key(MasterKey)
    Performance.set_StartTime(StartTime)
    Performance.set_EndTime(EndTime)
    PerformanceInfo = clt.do_action_with_exception(Performance)
    Info = (json.loads(PerformanceInfo))
    Value = Info['PerformanceKeys']['PerformanceKey'][0]['Values']['PerformanceValue'][-1]['Value']
    print  str(Value).split('&')[IndexNum]
def test(Key):
    if (Key == "MySQL_NetworkTraffic_In"):
        IndexNum = 0
        MasterKey = "MySQL_NetworkTraffic"
        GetPerformance(MasterKey,IndexNum,StartTime,EndTime)

    #平均每秒钟的输出流量
    elif (Key == "MySQL_NetworkTraffic_Out"):
        IndexNum = 1
        MasterKey = "MySQL_NetworkTraffic"
        GetPerformance(MasterKey,IndexNum,StartTime,EndTime)
    elif (Key == "other_size"):
        MasterKey = "MySQL_DetailedSpaceUsage"
        IndexNum = 4
        GetPerformance(MasterKey,IndexNum,StartTime,EndTime)
    elif (Key == "tmp_size"):
        MasterKey = "MySQL_DetailedSpaceUsage"
        IndexNum = 3
        GetPerformance(MasterKey,IndexNum,StartTime,EndTime)
# if __name__ == "__main__":
#     Key = sys.argv[1]
#     test1 = test(Key)
#     print test1
