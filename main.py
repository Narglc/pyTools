#coding:utf-8

import getPics
import saved_data
import analyse_page

def need_man_collect_pic_info():
    num_list = getPics.get_filter_pic_set_list()
    getPics.download_task("./pics/", saved_data.map_pics_download, num_list)
    getPics.show_error_info()

def half_auto_collect_pic_info():
    map_pic_info = analyse_page.get_pics_info_from_page_content(analyse_page.get_html_content())
    filter_list = getPics.get_filter_pic_set_list()
    getPics.download_task("./pics/", map_pic_info, filter_list)



if __name__ == '__main__':
    half_auto_collect_pic_info()