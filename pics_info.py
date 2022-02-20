#coding:utf-8
import os
from RedisHelper import RedisHelper

# 保存
def save_filter_list_to_file(filter_list, file_name):
    with open(file_name,"a+") as f:
        for it in filter_list:
            f.write(it+"\n")

def get_filter_list_from_file(file_name):
    filter_list = set()
    with open(file_name,"r") as f:
        line = f.readline()
        while line:
            filter_list.add(line[0:-1])
            line = f.readline()
    return filter_list

# 获取当前路径下已存在的套图列表
def get_filter_pic_set_list(pics_path):
    filter_list = set()
    all_dirs = os.listdir(pics_path)
    for cur_dir in all_dirs:
        tmp = cur_dir.split("_")
        filter_list.add(tmp[0])
    return filter_list

# 使用map存储套图信息
def get_pics_info_map_from_save_folder(pics_path):
    pics_info_map = []
    all_dirs = os.listdir(pics_path)
    for cur_dir in all_dirs:
        tmp = cur_dir.split("_")
        cur_pic_info = {
            "picSetNo"  :   tmp[0],
            "name"      :   tmp[1],
            "count"     :   len(os.listdir(pics_path+cur_dir))
        }
        pics_info_map.append(cur_pic_info)
    return pics_info_map

def save_pics_info_to_redis(pics_path, key_prefix, db = 1):
    redis_helper = RedisHelper(db)
    pic_map = get_pics_info_map_from_save_folder(pics_path)
    for each in pic_map:
        #print("%s-%s-%s"%(each["picSetNo"], each["name"], each["count"]))
        redis_helper.hmset(key_prefix+each["picSetNo"],each)