#coding:utf-8

import getPics
import saved_data
import analyse_page

pics_path = u"D:/FilesShare/pics/图集岛/"
filter_list_file_name = "filter_list.log"

def save_filter_list_to_file(file_name):
    getPics.save_filter_list_to_file(getPics.get_filter_pic_set_list(pics_path),file_name)

def get_filter_list_from_file(file_name):
    return getPics.get_filter_list_from_file(file_name)

def bak_filter_list():
    save_filter_list_to_file(filter_list_file_name)
    filter_list = get_filter_list_from_file(filter_list_file_name)
#    for it in filter_list:
#        print("[%s]"%it)
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
    print(len(map_pic_info))
    filter_list = get_filter_list_from_file(filter_list_file_name)
    getPics.download_task(pics_path, map_pic_info, filter_list)
    getPics.show_error_info()

if __name__ == '__main__':
    bak_filter_list()
    half_auto_collect_pic_info()