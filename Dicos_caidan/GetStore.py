#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/2020:10
import pymysql
import sys

def select_204store(storecode):
    con = pymysql.connect(host="172.16.5.204", user="root", password="dicos8888", database="dicos_ios")
    cur = con.cursor()
    sql = "select storecode,storename,address,phone,coordinate_X,coordinate_Y from store where storeCode = %s" % storecode
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    con.close()
    return  result

def select_218tstore(storecode):
    con = pymysql.connect(host="172.16.5.218", user="root", password="dicos8888", database="dicos_3rd")
    cur = con.cursor()
    sql = "select * from tstore where storeCode = %s" % storecode
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    con.close()
    return  result

def insert_store(storecode,storename,address,phone,coordinate_X,coordinate_Y):
    con = pymysql.connect(host="172.16.5.218", user="root", password="dicos8888", database="dicos_3rd")
    cur = con.cursor()
    sql= "INSERT INTO `dicos_3rd`.`tstore`(`id`, `storeCode`, `storeName`, `address`, `phone`, `coordinateX`, `coordinateY`, `channelOri`, `storeStatus`, `lastUpdateTime`, `operator`, `origin`, `email`, `starttime`, `endtime`, `shutMapTime`) VALUES (UUID(), '%s', '%s', '%s', '%s', '%s', %s, 'ALL', 1, NOW(), 'admin', '3rd', '825349215@qq.com', '07:00', '22:30', 0)" % (storecode,storename,address,phone,coordinate_X,coordinate_Y)
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
    decide_store = select_218tstore(storecode)
    print decide_store
    if len(decide_store) > 1:
        print "There are big problems with the basic information of this Store.Please check it %s： " % decide_store
    elif len(decide_store) == 1:
        print "The store's basic information exists"
    else:
        result = select_204store(storecode)
        if len(result) == 1:
            storecode = result[0][0]
            storename = result[0][1]
            address = result[0][2]
            phone = str(result[0][3])
            coordinate_X = str(result[0][4])
            coordinate_Y = str(result[0][5])
            insert_store(storecode, storename, address, phone, coordinate_X, coordinate_Y)
        else:
            print "The store information does not exist in the 204 database"

