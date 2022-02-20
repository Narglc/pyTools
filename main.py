#coding:utf-8

import getPics
import saved_data
import analyse_page
import pics_info
from RedisHelper import RedisHelper

pics_path =  "pics/"                       #u"D:/FilesShare/pics/图集岛/"
filter_list_file_name = "filter_list.log"

def save_filter_list_to_file(file_name):
    pics_info.save_filter_list_to_file(pics_info.get_filter_pic_set_list(pics_path),file_name)

def get_filter_list_from_file(file_name):
    return pics_info.get_filter_list_from_file(file_name)

def bak_filter_list(is_print = False):
    save_filter_list_to_file(filter_list_file_name)
    filter_list = get_filter_list_from_file(filter_list_file_name)
    if is_print:
        for it in filter_list:
            print("[%s]"%it)
    print("size:%d"%len(filter_list))

# 需要人工收集信息
def need_man_collect_pic_info():
    filter_list = get_filter_list_from_file(filter_list_file_name)
    getPics.download_task(pics_path, saved_data.map_pics_download, filter_list)
    getPics.show_error_info()

# 半自动收集,需要收集目录页html
def half_auto_collect_pic_info():
    map_pic_info = analyse_page.get_pics_info_from_page_content(analyse_page.get_html_content())
    for key,values in map_pic_info.items():
        print(key,values[0], values[1])
    print("共获取到%d个数据"%len(map_pic_info))
    filter_list = get_filter_list_from_file(filter_list_file_name)
    getPics.download_task(pics_path, map_pic_info, filter_list)
    getPics.show_error_info()


# 使用Redis进行过滤套图集, 并半自动收集
def half_auto_collect_pic_info_filter_by_redis(key_prefix):
    pics_info.save_pics_info_to_redis(pics_path, key_prefix)
    map_pic_info = analyse_page.get_pics_info_from_page_content(analyse_page.get_html_content())
    print("共获取到%d个数据"%len(map_pic_info))
    redis_helper = RedisHelper(1)
    for key,value in map_pic_info.items():
        if not redis_helper.exists(key_prefix+str(key)):
            print("Not exist info [", str(key), value[1])
            pic_set     = str(key)
            pic_count   = int(value[0])
            pic_name    = value[1]
            getPics.get_pic_set(pics_path, pic_set, pic_count, pic_name)
            break


if __name__ == '__main__':
    #bak_filter_list()
    #half_auto_collect_pic_info()
    half_auto_collect_pic_info_filter_by_redis("h_pics_tjd_")