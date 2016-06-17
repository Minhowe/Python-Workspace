# coding=utf-8
sstr = "123.xls"
pos_start = sstr.find("xls")
print pos_start
if pos_start > 0:
    sstr = sstr[0:pos_start]  #截取0到pos_tart字符串
    print sstr
    sstr = sstr[:pos_start]
    print sstr
    sstr = sstr[:pos_start-1]
    print sstr
#输出
# 4
# 123.
# 123.
# 123
# 请按任意键继续. . .