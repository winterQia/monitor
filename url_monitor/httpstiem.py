#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/516:09 

import re
import time
import subprocess
from datetime import datetime
from io import StringIO

def main(domain):
    f = StringIO()
    comm = "curl -Ivs https://{domain} --connect-timeout 10"
    result =subprocess.get
    f.write(result[1])

    m = re.search('start date: (.*?)\n.*?expire date: (.*?)\n.*?common name: (.*?)\n.*?issuer: CN=(.*?)\n', f.getvalue(), re.S)
    start_date = m.group(1)
    expire_date = m.group(2)
    common_name = m.group(3)
    issuer = m.group(4)

    # time 字符串转时间数组
    start_date = time.strptime(start_date, "%b %d %H:%M:%S %Y GMT")
    start_date_st = time.strftime("%Y-%m-%d %H:%M:%S", start_date)
    # datetime 字符串转时间数组
    expire_date = datetime.strptime(expire_date, "%b %d %H:%M:%S %Y GMT")
    expire_date_st = datetime.strftime(expire_date,"%Y-%m-%d %H:%M:%S")

    # 剩余天数
    remaining = (expire_date-datetime.now()).days

    print ('域名:', domain)
    print ('通用名:', common_name)
    print ('开始时间:', start_date_st)
    print ('到期时间:', expire_date_st)
    print ('剩余时间: {remaining}天')
    print ('颁发机构:', issuer)
    print ('*'*30)

    time.sleep(0.5)

if __name__ == "__main__":
    main('www.baidu.com')