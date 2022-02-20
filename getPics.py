from urllib import request
import time
import os

"""
from datetime import datetime
stime = datetime.now().strfttime("%H:%M:%S")
print("time:%s", stime)
"""

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
    print("\n")
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
        print("===== end of picSet:%s-%d ====="%(pic_set,pic_count))


def show_error_info():
    if error_info == None:
        print("all picSet Succ!")
    else:
        print("error_info:", end="")
        for key,values in error_info.items():
            print("%s/%d.jpg"%(key,values), end=",")
