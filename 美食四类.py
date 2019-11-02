#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

t1score=[]
t1id=[]
t2score=[]
t2id=[]
t3score=[]
t3id=[]
t4score=[]
t4id=[]

t1s=[]
t2s=[]
t3s=[]
t4s=[]



with open('A:\大三上\软件工程\团队编程实战\美食a版本/三坊七巷美食.json', 'r', encoding='utf-8') as f:
    data_back = json.load(f)
count=0
data=data_back["shop_list"]
for item in data:
    for i in item:
        jdata=i['detail_info']
        for j in jdata:
            if j=='price':
                for j1 in jdata:
                    if j1=='overall_rating':
                        for j2 in jdata:
                            if j2 == 'comment_num':
                                sum=eval(jdata['overall_rating'])*pow(1.01,eval(jdata['comment_num']))
                                pp=eval(jdata['price'])
                                if pp<50:
                                    t1id.append(i['name'])
                                    t1score.append(pp)
                                    t1s.append(sum)
                                elif pp>=50 and pp<100:
                                    t2id.append(i['name'])
                                    t2score.append(pp)
                                    t2s.append(sum)
                                elif pp>=100 and pp<200:
                                    t3id.append(i['name'])
                                    t3score.append(pp)
                                    t3s.append(sum)
                                elif pp>=200:
                                    t4id.append(i['name'])
                                    t4score.append(pp)
                                    t4s.append(sum)
        #score.append(jdata['overall_rating'])
        #for jitem in jdata:
        #    for j in jitem:
        #        print(j['rating'])
        count=count+1
        #score.append()
        #s1=i

print(count)

print(t1id)
print(t1score)
print(t1s)

print(t2id)
print(t2score)
print(t2s)

print(t3id)
print(t3score)
print(t3s)

print(t4id)
print(t4score)
print(t4s)

dic1 = dict(map(lambda x,y:[x,y],t1id,t1s))
dic2 = dict(map(lambda x,y:[x,y],t2id,t2s))
dic3 = dict(map(lambda x,y:[x,y],t3id,t3s))
dic4 = dict(map(lambda x,y:[x,y],t4id,t4s))
dic1 = sorted(dic1.items(),key = lambda k:k[1])
dic2 = sorted(dic2.items(),key = lambda k:k[1])
dic3 = sorted(dic3.items(),key = lambda k:k[1])
dic4 = sorted(dic4.items(),key = lambda k:k[1])
print(dic1)
print(dic2)
print(dic3)
print(dic4)

