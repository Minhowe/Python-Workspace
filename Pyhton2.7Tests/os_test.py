#coding=utf-8
import os
print os.getcwd() #get current work dir
os.chdir("C:\Users\Administrator\Desktop\Pyhton2.7Tests") #change dir
print os.getcwd()
print os.listdir(os.getcwd()) #filename list dir,return tuple
os.mkdir(os.getcwd() + "\\file") #make dir
os.rmdir(os.getcwd() + "\\file") #remove dir
#注意：删除目录需要说明的是，使用os.rmdir删除的目录必须为空目录，否则函数出错。
# 输出：
# D:\Program Files (x86)\Notepad++
# C:\Users\Administrator\Desktop\Pyhton2.7Tests
# ['chardet_test.py', 'chardet_test.txt', 'float2int.py', 'open_file_test.py', 'op
# en_file_test.txt', 'os_test.py', 'type_isinstance_test.py', 'unicode_str_test.py
# ']
# 请按任意键继续. . .