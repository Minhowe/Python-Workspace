# coding=utf-8
# import sys
# sstr = "name.js"
# print sstr[3:len(sstr)]

# arr = ["啊啊啊啊a", "b", "c", "d", "e"] 
# print len(arr)

# sstr = "<1008,3><population,500>"
# print sstr.split(">")
# <1008,3> <treats, 120>
# {
#  "key":"1008",
#  "value":3
# },
# {
#  "key":"treats",
#  "value":120
# },
value = "<1008,3> <treats, 120>"
# setting = ""
# setting.left = "<"
# setting.right = ">"
# setting.dot = ","

pos_left = value.find("<")
if pos_left >= 0:
    pos_right = value.find(">")
    if pos_right > 0:
        pos_dot = value.find(",")
        if pos_dot > 0:
            value = value.lstrip("<") # 1008,3> <treats, 120>        
            value_list = value.split("<")   # ['1008,3> ', 'treats, 120>']
            elif len(value_list) == 1:
                item = value_list[0]  # 1008,3>
                item = item.rsplit(">") # ['1008','3']
                item = item[0].split(",")  # ['1008','3']
                dic = dict()
                dic["value"] = item[1]
                dic["key"] = item[0]
                print dic
            elif len(value_list) > 1: 
                list = []
                for i in xrange(0 , len(value_list)):
                    item = value_list[i]      # 1008,3>
                    item = item.rsplit(">")   # delete '>'
                    item = item[0].split(",") # ['1008','3']
                    dic = dict()
                    dic["value"] = item[1]
                    dic["key"] = item[0]    
                    list.append(dic)           
                print list
