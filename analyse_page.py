#encoding:utf-8

import requests
import re

url = "https://www.tujidao.com/t/?id=298"

def get_html_content():
    page_content = ""
    with open("page.html","r", encoding="utf-8") as f:
        page_content = f.read()
    return page_content
'''
    rsp = requests.get(url)
    print(rsp.text)
'''


def get_pics_info_from_page_content(page_content):
    map_pic_info = {}
    pic_list = re.findall("<li id=.*?</li>",page_content,re.S)
    for pic_html in pic_list:
        pic_set   = re.findall('<li id="(.*?)">',pic_html,re.S)[0]
        pic_count = re.findall('<span class="shuliang">(.*?)P</span>',pic_html, re.S)[0]
        pic_name  = re.findall(r'><a href=.*?>(.*?)</a></p>', pic_html, re.S)[0].strip()
        map_pic_info[pic_set] = [pic_count, pic_name]
    return map_pic_info

'''
page_content = get_html_content()
map_pic_info = get_pics_info_from_page_content(page_content)

for key,values in map_pic_info.items():
    print(key,values[0], values[1])
'''
