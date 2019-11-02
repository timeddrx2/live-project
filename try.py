import json
with open('E:\程序\软工\python\py\美食a版本\左海美食.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

data = t["shop_list"]
sum = 0
count1 = 0

for i in data:
    for store in i:
        detail_info = store["detail_info"]
        if ("overall_rating" in detail_info):
            sum = sum + float(detail_info["overall_rating"])
            count1 =count1+1;
        else:
            print("无评论数")
            count1 = count1 + 1;
count2=float(sum/float(count1))
title = "1"
f = open('%s.txt' % title, 'w', encoding='utf-8')
f.writelines("仓前美食");
f.writelines(str(count2));
f.write("\n")
