# coding=utf-8
import sys
def get_cur_info():
    print sys._getframe().f_code.co_name
    print sys._getframe().f_lineno
    print sys._getframe().f_back.f_code.co_name
get_cur_info()

# log:
# get_cur_info
# 5
# <module>