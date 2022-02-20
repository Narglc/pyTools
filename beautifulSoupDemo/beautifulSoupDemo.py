#coding:utf-8

import re
import requests
from bs4 import BeautifulSoup

"""
url = "https://www.jpg12345.net/tao/3/43357.html"

str_html = requests.get(url)

# 指定网页的编码格式
str_html.encoding = 'gbk'

'''
使用 Beautiful Soup 解析网页
环境准备:
    需要安装库bs4,lxml,可使用命令`pip3 install bs4 lxml
'''

# 将复杂的HTML文档转换成树形结构，且每个结点都是Python对象; 并置顶使用lxml解析器,python自带解析器会失败
soup = BeautifulSoup(str_html.text,'lxml')

# selet定位器 定位数据
data = soup.select("body > div.content > img")

#print(data)
print("type data",type(data))
list = []
for item in data:
    result={
        'title':item.get('alt'),                    # 获取文字内容
        'link':item.get('src'),
        #'ID':re.findall('\d+', item.get("src"))
    }
    list.append(result)

for item in list:
    print(item)
"""



'''
# 2. 通过本地html 文件来创建对象
soup2 = BeautifulSoup(open('soup_demo.html'), "lxml")

# 格式化输出
#print(soup2.prettify())                                 

# 输出第一个 title 标签
print(soup2.title)
print(soup2.title.name)
print(soup2.title.string)

print(soup2.p['class'])
print(soup2.a['href'])

print(soup2.find_all('a'))
print(soup2.find(id="link3"))

print(soup2.get_text())

for link in soup2.find_all('a'):
    # 获取 link 的 href 属性内容
    print(link.get('href'))

#对soup.p的子节点进行循环输出    
for child in soup2.p.children:
    print(child)
 
#正则匹配，名字中带有b的标签
for tag in soup2.find_all(re.compile("b")):
    print(tag.name)
'''

# 3. 使用bs解析tjd
lsp = BeautifulSoup( open('../page.html', encoding='utf-8'),'lxml')
data = lsp.select("body > div > ul")
pic_info = []
for item in data:
    if item.span == None:
        continue
    all_li = item.select("li")
    for each_li in all_li:
        result = {
            "picSetNo":each_li.get("id"),
            "shuliang":each_li.span.get_text()[:-1],
            "name":each_li.select('li > p > a')[-1].get_text()
        }
        print(result)
        pic_info.append(result)


# 4. 保存到 Redis
import redis
r = redis.Redis(host='localhost',port=6379,db=0)
for item in pic_info:
    str_key = "hpics_tjd_%s"%(item["picSetNo"])
    r.hset(str_key, "name", item["name"])
    r.hset(str_key, "count",item["shuliang"])
