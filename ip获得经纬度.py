import requests
import json
def login(account):
    url='https://api.map.baidu.com/location/ip'
    form_data={
        "ip": account["ip"],
        "ak": account["ak"],
        "coor":account["coor"]
    }
#    form_data = {"ip": "101.247.112.18", "ak": 'dntnIGs3ueWbi8TGkGYz0l8j1p6c9Yc1', "coor": "bd09ll"}
    print(form_data)
    headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    }
    response=requests.post(url=url,headers=headers,data=form_data,verify=False);
    return response.text.encode('utf-8').decode('unicode_escape')
account=dict()
account['ip']=''
account['ak']='dntnIGs3ueWbi8TGkGYz0l8j1p6c9Yc1'
account['coor']='bd09ll'
t=login(account)
print(t)
#{"status":0,"data":{"user_id":4,"token":"8727cb46-81dc-4719-b043-bb76532171fc"}}
