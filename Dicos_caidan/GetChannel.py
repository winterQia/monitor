#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/1917:41 
import pymysql
import  sys
import conn_mysql

def select_channel(storecode):
    con = pymysql.connect(host="172.16.5.204", user="root", password="dicos8888", database="dicos_ios")
    cur = con.cursor()
    sql = "select * from t_storechannel where storeCode = %s" % storecode
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    con.close()
    return result
def insert_channel(storecode):
    con = pymysql.connect(host="172.16.5.204", user="root", password="dicos8888", database="dicos_ios")
    cur = con.cursor()
    sql1 = "INSERT INTO `dicos_ios`.`t_storechannel`(`channel`, `storeCode`, `startTime`, `endTime`, `deliveryType`, `status`, `shutReason`, `shutMapTime`, `consignerId`, `consignerShowName`, `serviceFeeRate`) VALUES ( 1, %s, '07:30', '23:59', '2', '1', NULL, NULL, NULL, NULL, null)" % storecode
    sql2 = "INSERT INTO `dicos_ios`.`t_storechannel`(`channel`, `storeCode`, `startTime`, `endTime`, `deliveryType`, `status`, `shutReason`, `shutMapTime`, `consignerId`, `consignerShowName`, `serviceFeeRate`) VALUES ( 2, %s, '07:30', '23:59', '2', '1', NULL, NULL, NULL, NULL, null)" % storecode
    sql3 = "INSERT INTO `dicos_ios`.`t_storechannel`(`channel`, `storeCode`, `startTime`, `endTime`, `deliveryType`, `status`, `shutReason`, `shutMapTime`, `consignerId`, `consignerShowName`, `serviceFeeRate`) VALUES ( 3, %s, '07:30', '23:59', '2', '1', NULL, NULL, NULL, NULL, null)" % storecode
    sql4 = "INSERT INTO `dicos_ios`.`t_storechannel`(`channel`, `storeCode`, `startTime`, `endTime`, `deliveryType`, `status`, `shutReason`, `shutMapTime`, `consignerId`, `consignerShowName`, `serviceFeeRate`) VALUES ( 4, %s, '07:30', '23:59', '2', '1', NULL, NULL, NULL, NULL, null)" % storecode
    sql5 = "INSERT INTO `dicos_ios`.`t_storechannel`(`channel`, `storeCode`, `startTime`, `endTime`, `deliveryType`, `status`, `shutReason`, `shutMapTime`, `consignerId`, `consignerShowName`, `serviceFeeRate`) VALUES ( 5, %s, '07:30', '23:59', '2', '1', NULL, NULL, NULL, NULL, null)" % storecode

    try:
        cur.execute(sql1)
        cur.execute(sql2)
        cur.execute(sql3)
        cur.execute(sql4)
        cur.execute(sql5)
    except Exception as e:
        con.rollback()
        print "Transaction failure",e
    else:
        con.commit()
        print "Transaction success"
    cur.close()
    con.close()

def chose(kinds,storecode):

    if kinds == 'select':
      print   select_channel(storecode)
    elif kinds == 'insert':
        insert_channel(storecode)



if __name__ == "__main__":
    kinds = sys.argv[1]
    storecode = sys.argv[2]
    chose(kinds,storecode)
