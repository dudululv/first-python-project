import requests
from lxml import etree  #导包
import time,random
#访问 一个地址
url='https://miaoso.com/bus/beijing/suoyin-xianlu-daquan.html'
resp=requests.get(url)
print(resp)  #<Response [200>]  200是请求成功的意思
print(resp.status_code) #200 状态码
# print(resp.text) #查看页面内容
tree=etree.HTML(resp.text) #变成树形结构
print(tree)
# #/ 单斜杠开头是绝对路径 //双斜杠是相对路径  *是里面的都要   //BBB[@*] B标签所有带有属性的都要
list1=[]
for i in range(1,28,1):
    list1.append('https://miaoso.com/bus/beijing/'+tree.xpath(f'//dl[@class="f-cb"][1]/dd[{i}]/a/@href')[0])
    # break
print(list1)  #拿到所有的1开头,2开头....地址
dict1={}
for i in list1:
    resp=requests.get(i)
    tree=etree.HTML(resp.text)
    urls=tree.xpath('//div[@class="list"][2]/ul[@class="f-cb"]/li/a/@href')
    titles=tree.xpath('//div[@class="list"][2]/ul[@class="f-cb"]/li/a/@title')
    print(urls[0],titles[0])
#     index=0
#     for j in urls:
#         r=requests.get('https://miaoso.com/bus/beijing/'+j)
        
#         t=etree.HTML(r.text)
#         a=t.xpath('//ul[@id="x1"]//a/text()')
#         print(titles[index]) #{'101路(百万庄西口-红庙路口东)':['红庙路口东'，'红庙路口西',,]}
#         dict1[titles[index]]=a
#         time.sleep(random.uniform(1.5,5.5))
#         index+=1
#         break
#     break
# print(dict1)
# with open('公交线路.txt','w',encoding='utf-8') as file:
#     for k,v in dict1.items():
#       file.write(k+':'+'-'.join(v)+'\n')
#     #break