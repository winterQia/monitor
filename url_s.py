import requests
import time

url_list = ["http://172.16.4.74:9082/menu.service/cc?brand=dicos_test&clearType=0",
            "http://172.16.4.75:9082/menu.service/cc?brand=dicos_test&clearType=0",
            "http://172.16.4.76:9082/menu.service/cc?brand=dicos_test&clearType=0",
            "http://172.16.4.78:9082/menu.service/cc?brand=dicos_test&clearType=0",
            "http://172.16.4.79:9082/menu.service/cc?brand=dicos_test&clearType=0",
            "http://172.16.2.143:9082/menu.service/cc?brand=dicos_test&clearType=0",
            "http://172.16.2.146:9082/menu.service/cc?brand=dicos_test&clearType=0"]
url_list1 = ["http://172.16.4.74:9082/menu.service/cc?brand=dicos_test&clearType=1",
             "http://172.16.4.75:9082/menu.service/cc?brand=dicos_test&clearType=1",
             "http://172.16.4.76:9082/menu.service/cc?brand=dicos_test&clearType=1",
             "http://172.16.4.78:9082/menu.service/cc?brand=dicos_test&clearType=1",
             "http://172.16.4.79:9082/menu.service/cc?brand=dicos_test&clearType=1",
             "http://172.16.2.146:9082/menu.service/cc?brand=dicos_test&clearType=1",
             "http://172.16.2.143:9082/menu.service/cc?brand=dicos_test&clearType=1"]


def get_url():
    for i in range(len(url_list)):
        req = requests.get(url=url_list[i])
        p_url = req.url
        p_status = req.status_code
        print ("The URL you visited:%s , His state is:%s" % (p_url, p_status))


def get_url1():
    for i in range(len(url_list1)):
        req = requests.get(url=url_list1[i])
        p_url = req.url
        p_status = req.status_code
        print ("The URL you visited:%s , His state is:%s" % (p_url, p_status))


if __name__ == "__main__":
    get_url()
    time.sleep(5)
    get_url1()
