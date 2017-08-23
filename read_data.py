#!/usr/bin/python2.7
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

with open('WMdata.dat.1', 'r') as file:
    for line in file:
        view = line.split()
        app_id = view[0]
        src_user_id = view[1]
        view_user_id = view[2]
        province = view[3]
        date = int(view[4])
        time = int(view[5])
        duration = int(view[6])
        viewed_page_num = int(view[7])
        total_page_num = int(view[8])
        # do something you like