import redis

def total():
    r=redis.Redis(host='r-uf6363489a4b1514.redis.rds.aliyuncs.com',port='6379',password='Ilovebk2016')
    total=r.dbsize()
    print total
total()