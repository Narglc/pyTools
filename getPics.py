from urllib import request
import time
import os

"""
from datetime import datetime
stime = datetime.now().strfttime("%H:%M:%S")
print("time:%s", stime)
"""

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

# 图集岛网址
img_base_url =  u"https://tjg.gzhuibei.com/a/1/"

# 记录下载出错的图片
error_info = {}

# 具体下载某一套图集
def get_pic_set(local_save_base_path, set_info_path, pics_num, pic_name = None):
    local_save_path = local_save_base_path + set_info_path + "_"
    if not os.path.exists(local_save_path):
        os.mkdir(local_save_path)

    for i in range(1,pics_num+1):
        curPicUrl = img_base_url + set_info_path + "/" + str(i) + ".jpg"
        #print("downing " + curPicUrl)
        print("#", end="")
        try:
            request.urlretrieve(curPicUrl,'%s/%d.jpg'%(local_save_path,i))
        except:
            error_info[set_info_path] = i
            return
        else:
            pass
            #time.sleep(0.01)
    if pic_name != None:
        os.rename(local_save_path,local_save_path+pic_name)


# 下载任务
def download_task(local_save_base_path, map_pics_download, num_list = None):
    for key,values in map_pics_download.items():
        pic_set     = str(key)
        pic_count   = int(values[0])
        pic_name    = values[1]
        if num_list != None:                # 设置过滤项
            if pic_set in num_list:
                continue
        print("downloading foldor:%s, num:%d pic_name:%s..."%(pic_set, pic_count,pic_name))    
        get_pic_set(local_save_base_path, pic_set, pic_count, pic_name)        # 下载图集
        print("\n===== end of picSet:%s-%d ====="%(pic_set,pic_count))


def show_error_info():
    if error_info == None:
        print("all picSet Succ!")
    else:
        print("error_info:", end="")
        for key,values in error_info.items():
            print("%s/%d.jpg"%(key,values), end=",")
