import requests
from lxml import etree  #导包
import time,random
url='https://movie.douban.com/top250?start=0&filter='
h={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'
}
# resp=requests.get(url,headers=h)
# print(resp.status_code)
# t=etree.HTML(resp.text)
# # tx=t.xpath('//div[@class="title"]/a/text()')
# tx = t.xpath('//div[@class="hd"]/a/span[@class="title"][1]/text()')

# print(tx)
# # titles_clean = [title.strip() for title in tx]
# # print(titles_clean)
idx=1
dict1={}
for i in range(0,230,25):
    url=f'https://movie.douban.com/top250?start={i}&filter='
    resp=requests.get(url,headers=h)
#     # print(resp.status_code)
    t=etree.HTML(resp.text)
#     # cname=t.xpath('//div[@class="title"]/a/text()')
    dict1[f'{idx}']=t.xpath('//div[@class="hd"]/a/span[@class="title"][1]/text()')
    idx+=1
    time.sleep(random.uniform(2,4))
print(dict1)
