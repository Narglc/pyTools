#coding:utf-8

from urllib import request
import re
import time
import os

with open("meizitu.html", "r", encoding="utf-8") as f:
    html_content = f.read()

pic_list = re.findall(u'</a></span><p><a href="(.*?)" target="_blank" class="view_img_link"', html_content)

#print(pic_list)    
print(len(pic_list))

filter_list = os.listdir("meizitu")
#print(filter_list)
print(len(filter_list))


is_need_sleep = 0
for pic_part_url in pic_list:
    name = pic_part_url.split("/")[-1]
    if name in filter_list:
        continue
    is_need_sleep = is_need_sleep + 1
    print(is_need_sleep, name)
    request.urlretrieve("http:"+pic_part_url,'meizitu/'+name)
    if is_need_sleep == 20:
        time.sleep(0.1)



