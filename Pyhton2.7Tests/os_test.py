#coding=utf-8
import os
print os.getcwd() #get current work dir
os.chdir("C:\Users\Administrator\Desktop\Pyhton2.7Tests") #change dir
print os.getcwd()
print os.listdir(os.getcwd()) #filename list dir,return tuple
os.mkdir(os.getcwd() + "\\file") #make dir
os.rmdir(os.getcwd() + "\\file") #remove dir
#ע�⣺ɾ��Ŀ¼��Ҫ˵�����ǣ�ʹ��os.rmdirɾ����Ŀ¼����Ϊ��Ŀ¼������������
# �����
# D:\Program Files (x86)\Notepad++
# C:\Users\Administrator\Desktop\Pyhton2.7Tests
# ['chardet_test.py', 'chardet_test.txt', 'float2int.py', 'open_file_test.py', 'op
# en_file_test.txt', 'os_test.py', 'type_isinstance_test.py', 'unicode_str_test.py
# ']
# �밴���������. . .