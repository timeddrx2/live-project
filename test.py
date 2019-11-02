import requests
import json
import time

def get_groundinfo():
    url='http://api.map.baidu.com/place/v2/search?query=商圈&region=福州&output=json&page_size=100&scope=2&ak=dntnIGs3ueWbi8TGkGYz0l8j1p6c9Yc1'
    # data = {
    #     'query' : '商圈',
    #     'output' : 'JSON',
    #     'page_size' : '20',
    #     'scope' : '2',
    #     'ak' : 'dntnIGs3ueWbi8TGkGYz0l8j1p6c9Yc1',
    # }

    # json_data = {'shop_list':[]}
    #print(type(res))
    
    #res = json.dumps(res,indent=4,ensure_ascii=False)
    res = requests.get(url)
    # print(res)
    # res = res.text
    res = res.json()
    print(res)
    json_data = json.dumps(res,indent=4,ensure_ascii=False)
    fileObject = open('商圈.json', 'w', encoding='utf-8')
    fileObject.write(json_data)
    fileObject.close()
    print(res)

# get_groundinfo()

def get_shopinfo():
    with open("商圈.json",'r',encoding='utf-8') as f:
        load_dict = json.load(f)
    fname = ""
    location = ''
    s = load_dict['results']
    for item in s:
        time.sleep(3)
        fname = item['name'] + '服饰' + '.json'
        location = str(item['location']['lat']) + ',' + str(item['location']['lng'])
        url = "http://api.map.baidu.com/place/v2/search" 
        #url='http://api.map.baidu.com/place/v2/search?query=奶茶&location=26.0566457738,119.1983916599&scope=2&page_num=2&radius=9000&output=json&page_size=100&ak=dntnIGs3ueWbi8TGkGYz0l8j1p6c9Yc1'
        data = {
            'query':'服饰',
            'location' : '26.116406394259,119.31224373667',
            'page_num' : '1',
            'output' : 'json',
            'page_size' : '20',
            'scope' : '2',
            'ak' : 'zGMqYhaaRzyYGMIzETY457hRGz4xdKSw',
            'radius' : '500'
        }
        data['location'] = location
        json_data = {'shop_list':[]}
        #print(type(res))
        for i in range(5):
            time.sleep(3)
            #res = json.dumps(res,indent=4,ensure_ascii=False)
            print(data['page_num'])
            res = requests.get(url=url,params=data)
            #res = res.json()
            res= res.json()
            print(type(res))
            print(res)
            json_data['shop_list'].append(res['results'])
            #print(res['resultes'])
            data['page_num'] = str(int(data['page_num']) + 1)
        json_data = json.dumps(json_data,indent=4,ensure_ascii=False)
        fileObject = open(fname, 'w', encoding='utf-8')
        fileObject.write(json_data)
        fileObject.close()
        print(res)

get_shopinfo()
