#coding:utf-8

import getPics
import saved_data

def main():
    num_list = getPics.get_pic_set_list()
    getPics.download_task("./pics/", saved_data.map_pics_download, num_list)


if __name__ == '__main__':
    main()