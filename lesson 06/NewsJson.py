
import json
import requests

news_list = [] # 資料要先整理到集合中，所以要先開一個空集合
url = 'http://oldpaper.g0v.ronny.tw/index/json?fbclid=IwAR1zip-1_wLBrsZ2p9RfiAjm-WeFaxb8UyI4nA-uXOhK6Q3Wkgn7D_Zukow'
data = json.loads(requests.get(url).text)

for d in data.get('data'):
    dict = {'title':d.get('title'), 'headlines':d.get('headlines')}
    news_list.append(dict)

# print(news_list)
#找 關鍵字 "貸款"

file = open('news2.txt', 'a')
for news in news_list:
    for head in news['headlines']:
        if '紓困' in head[1]:
            print(head)
            file.writelines(head)
            file.write("\n")