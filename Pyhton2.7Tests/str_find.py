# coding=utf-8
sstr = "123.xls"
pos_start = sstr.find("xls")
print pos_start
if pos_start > 0:
    sstr = sstr[0:pos_start]  #��ȡ0��pos_tart�ַ���
    print sstr
    sstr = sstr[:pos_start]
    print sstr
    sstr = sstr[:pos_start-1]
    print sstr
#���
# 4
# 123.
# 123.
# 123
# �밴���������. . .