import requests
import json

a = ['rabbit@sql5-209','rabbit@sql5-210','rabbit@sql5-211']
def GetMqnodes():
    name = []
    url = 'http://172.16.5.209:15672/api/nodes'
    r = requests.get(url, auth=("guest", "guest"), timeout=5)
    parsed = json.loads(r.content)
    namelen = len(parsed)

    if namelen < 3 :
        for i in parsed:
            name.append(i.get('name'))
        for i in range(0, len(a)):
            if a[i] not in name:
                print a[i]
    else:
        print namelen


if __name__ == "__main__":
    GetMqnodes()
