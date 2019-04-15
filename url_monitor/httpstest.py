#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/621:18
import OpenSSL
import time
import parser

import datetime
t = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, open("D:\crt\Bkpaymar\Bkpaymgr.pem").read())
#t2 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, open("C:\Users\ASUS\Desktop\qxd.pem").read())
t1 = t.get_issuer()
# print t.get_notBefore(), t2.get_notBefore()
#print t.get_notAfter(), t2.get_notAfter()
Due_time=str(t.get_notAfter())
Due_year=str(Due_time[0:4])
Due_date=str(Due_time[4:6])
locat_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
local_year = str(locat_time[0:4])
locat_date = str(locat_time[4:6])
if local_year >= Due_date:
    alarm = int(Due_date) - int(locat_date)
    print alarm
else:
    print 12