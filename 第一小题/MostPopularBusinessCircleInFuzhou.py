#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

list = []

with open('万宝商圈.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "万宝商圈"]
list.append(temp)

with open('万宝商圈联防联动指挥中心.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "万宝商圈联防联动指挥中心"]
list.append(temp)

with open('三坊七巷.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "三坊七巷"]
list.append(temp)

with open('东二环泰禾.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "东二环泰禾"]
list.append(temp)

with open('仓前.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "仓前"]
list.append(temp)

with open('仓山万达.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "仓山万达"]
list.append(temp)

with open('台江万达.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "台江万达"]
list.append(temp)

with open('吴航.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "吴航"]
list.append(temp)

with open('左海.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "左海"]
list.append(temp)

with open('火车南站.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "火车南站"]
list.append(temp)

with open('王府井.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "王府井"]
list.append(temp)

with open('甘蔗.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "甘蔗"]
list.append(temp)

with open('省体育中心.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "省体育中心"]
list.append(temp)

with open('西湖公园.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "西湖公园"]
list.append(temp)

with open('金逸影城(万宝商圈店).json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "金逸影城(万宝商圈店)"]
list.append(temp)

with open('金逸影城IMAX(万宝商圈店).json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "金逸影城IMAX(万宝商圈店)"]
list.append(temp)

with open('龙院.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0
count2 = 0
for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("comment_num" in detail_info):
            sum = sum + int(detail_info["comment_num"])
            count1 = count1 + 1
        else:
            # print("无评论数")
            count2 = count2 + 1
temp = [sum, "龙院"]
list.append(temp)

list.sort(reverse=True)
print(list)
