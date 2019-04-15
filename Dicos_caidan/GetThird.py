#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/2021:08
import pymysql
import sys

def select_tstoremap(storecode):
    con = pymysql.connect(host="172.16.5.218", user="root", password="dicos8888", database="dicos_3rd")
    cur = con.cursor()
    sql = "SELECT * from tstoremap where storeCode in (%s)" % storecode
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    con.close()
    return  result

def insert_tstoremap_ELEME(storecode,third):
    con = pymysql.connect(host="172.16.5.218", user="root", password="dicos8888", database="dicos_3rd")
    cur = con.cursor()
    sql= "INSERT INTO `dicos_3rd`.`tstoremap`(`id`, `storeCode`, `thirdStoreCode`, `status`, `brand`, `delayTime`, `isChannelClose`, `merchantNo`, `channel`, `areaRange`, `markerImg`, `isAutoOrder`, `announcement`, `announcementTag`, `startTime`, `endTime`, `openStatus`, `openTime`, `thirdStoreId`, `baseTime`) VALUES (UUID(), %s, %s, 1, 'DICOS', 0, 1, 'dicosprochn', 'ELEME', NULL, NULL, NULL, '德克士新店开业，欢迎光临！', 1, NULL, NULL, 1, NOW(),NULL, 40)" % (storecode,third)
    try:
        cur.execute(sql)
    except Exception as e:
        con.rollback()
        print "Transaction failure", e
    else:
        con.commit()
        print "Transaction success"
    cur.close()
    con.close()

def insert_tstoremap_MEITUAN(storecode,third):
    con = pymysql.connect(host="172.16.5.218", user="root", password="dicos8888", database="dicos_3rd")
    cur = con.cursor()
    sql= "INSERT INTO `dicos_3rd`.`tstoremap`(`id`, `storeCode`, `thirdStoreCode`, `status`, `brand`, `delayTime`, `isChannelClose`, `merchantNo`, `channel`, `areaRange`, `markerImg`, `isAutoOrder`, `announcement`, `announcementTag`, `startTime`, `endTime`, `openStatus`, `openTime`, `thirdStoreId`, `baseTime`) VALUES (UUID(), %s, %s, 1, 'DICOS', 0, 1, 'dicosprochn', 'MEITUAN', NULL, NULL, NULL, '德克士新店开业，欢迎光临！', 1, NULL, NULL, 1, NOW(),NULL, 40)" % (storecode,third)
    try:
        cur.execute(sql)
    except Exception as e:
        con.rollback()
        print "Transaction failure", e
    else:
        con.commit()
        print "Transaction success"
    cur.close()
    con.close()

if __name__ == "__main__":
    storecode = sys.argv[1]
    result = select_tstoremap(storecode)
    if len(result) == 2 :
        print "Please make sure that your %s %s is %s correct" % (result[0][1],result[0][8],result[0][2])
        print "Please make sure that your %s %s is %s correct" % (result[1][1],result[1][8],result[1][2])
    elif len(result) == 1 :
        print "Please make sure that your %s %s is %s correct" % (result[0][1], result[0][8], result[0][2])
        if result[0][8] == "ELEME":
            third = sys.argv[2]
            insert_tstoremap_MEITUAN(storecode,third)
        else:
            third = sys.argv[2]
            insert_tstoremap_ELEME(storecode,third)

    # elif len(result) == 0:
    #     print "now,There is no third party account in this restaurant."
        # storecode = input("Please input your storecode: ")
        # third = input("Please input your third: ")
        # thirdname = str(raw_input("Please input your thirdname: "))
        #
        # insert_tstoremap(storecode,third,thirdname)


