# coding=utf-8
SUFFIX = "xls"
path = "name.xls"
pos_start = path.find(SUFFIX) - 1
js_name = path[:pos_start] + "_Josn.js"
print js_name
print "''"
print '""'
print path[:pos_start]
print '"path[:pos_start]"'
print '"'+ path[:pos_start] +'"'
# 输出：
# name_Josn.js
# ''
# ""
# "path[:pos_start]"
# "name"
# 请按任意键继续. . .