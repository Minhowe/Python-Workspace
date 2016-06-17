# -*- coding: UTF-8 -*-
a = 1.0
sstr = str(a)
print sstr
pos_start = sstr.find(".")
if pos_start > 0:
    sstr = sstr[0:pos_start]  #截取0到pos_tart字符串
    print int(sstr)
    if(int(sstr) == a):
        a = int(sstr) 
    else:
        a = a 
    
print a 