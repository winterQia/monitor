#!/usr/bin/python
# encoding=utf-8

from aliyunsdkcore.client import AcsClient
import json
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkrds.request.v20140815 import DescribeResourceUsageRequest
from aliyunsdkrds.request.v20140815 import DescribeDBInstancePerformanceRequest
from aliyunsdkrds.request.v20140815 import DescribeDBInstanceMonitorRequest
from aliyunsdkrds.request.v20140815 import ModifyDBInstanceMonitorRequest
from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest
import json
AcesskeyID = 'LTAIk1fHVSSahLxN'
AcesskeySecret = 'usd1W47lTFXhhTIR5Cq5WTw9M3qACg'
regionid = 'cn-hangzhou'
client = AcsClient(
    AcesskeyID,
    AcesskeySecret,
    regionid)
DBInstanceIdList = []
DBInstanceIdDict = {}
ZabbixDataDict = {}
def GetRdsList():
    RdsRequest = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
    RdsRequest.set_accept_format('json')
    RdsRequest.set_DBInstanceId('rm-bp18144qkyj20731o')
    RdsInfo = json.loads(client.do_action_with_exception(RdsRequest))
    print RdsInfo
    for RdsInfoJson in RdsInfo["Items"]["DBInstance"]:
        DBInstanceIdDict = {}
        DBInstanceIdDict["{#DBINSTANCEID}"] = RdsInfoJson['DBInstanceId']
        #print DBInstanceIdDict["{#DBINSTANCEID}"]
        DBInstanceIdDict["{#InsId}"] = RdsInfoJson['InsId']
        #print DBInstanceIdDict["{#InsId}"]
        DBInstanceIdList.append(DBInstanceIdDict)

#    print RdsInfo["Items"]["DBInstance"][0]["LockMode"]

    # for key,value in RdsInfo.items():
    #     if isinstance(value,dict):
    #         for key, value_list in RdsInfo.items():
    #             print key,value_list
    #             if isinstance(value, dict):
    #                 for key, value in value.items():
    #                     print key, value
    #                     for v_list in value:
    #             #             for key,list_2 in v_list.items():
    #             #                 print key,list_2
    #             # #                 if isinstance(value, dict):
    #             # #                     for key, value in value.items():
    #             # # #                         # print key, value
    #             # # #
                # # # #
                # # #
                # # # for value in value_list:
                #     print value

        # print value
    # for RdsInfoJson in RdsInfo:
    #     print RdsInfoJson







def DRUR():
    request = DescribeResourceUsageRequest.DescribeResourceUsageRequest()
    request.set_accept_format('json')
    request.set_DBInstanceId('rm-bp18144qkyj20731o')
    response = json.loads(client.do_action_with_exception(request))
    for key,values in response.items():
        print (str(key) + '=' + str(unicode(values)))


def MDBMR():

    request1 = ModifyDBInstanceMonitorRequest.ModifyDBInstanceMonitorRequest()
    request1.set_accept_format('json')
    request1.set_DBInstanceId('rm-bp18144qkyj20731o')
    request1.set_Period('60')
    response1 = client.do_action_with_exception(request1)
    print response1

if __name__ == "__main__":
    GetRdsList()
    ZabbixDataDict['data']=DBInstanceIdList
    print ZabbixDataDict