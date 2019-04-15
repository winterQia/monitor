#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/711:29 
import pymysql
import sys

def rds_orderinfo():
    con = pymysql.connect(host="rm-uf69x5vn5nqg321bg.mysql.rds.aliyuncs.com", user="chc_order_dbuser", password="Ilovebk2016", database="chc_order_db")
    cur = con.cursor()
    sql = "SELECT count(*) FROM  `sf_orderinfo`"
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    con.close()
    return result[0][0]

def rds_orderdetail():
    con = pymysql.connect(host="rm-uf69x5vn5nqg321bg.mysql.rds.aliyuncs.com", user="chc_order_dbuser", password="Ilovebk2016", database="chc_order_db")
    cur = con.cursor()
    sql = "SELECT count(*) FROM  `sf_orderdetail`"
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    con.close()
    return result[0][0]

def rds_crmorderdetail():
    con = pymysql.connect(host="rm-uf69x5vn5nqg321bg.mysql.rds.aliyuncs.com", user="chc_order_dbuser", password="Ilovebk2016", database="chc_order_db")
    cur = con.cursor()
    sql = "SELECT count(*) FROM  `sf_crmorderdetail`"
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    con.close()
    return result[0][0]

def rds_crmorderinfo():
    con = pymysql.connect(host="rm-uf69x5vn5nqg321bg.mysql.rds.aliyuncs.com", user="chc_order_dbuser", password="Ilovebk2016", database="chc_order_db")
    cur = con.cursor()
    sql = "SELECT count(*) FROM  `sf_crmorderinfo`"
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    con.close()
    return result[0][0]


def Get_sql(kinds):
    if kinds == "orderinfo":
        print rds_orderinfo()
    elif kinds == "crmorderinfo":
        print rds_crmorderinfo()
    elif kinds == "crmorderdetail":
        print rds_crmorderdetail()
    elif kinds == "orderdetail":
        print rds_orderdetail()

if __name__ == "__main__":
    kinds = sys.argv[1]
    Get_sql(kinds)


