#coding=utf-8
#�½��ļ�open_file_test.txt���ݣ�
# Hello World
# This is a test file
import os
print os.getcwd()
os.chdir("C:\Users\Administrator\Desktop\Pyhton2.7Tests")
test = [ "test1\n", "test2\n", "test3\n" ]
f = open("open_file_test.txt", "a+")
try:
 #f.seek(0)
 for l in test:
  f.write(l)
finally:
 f.close()
# �����
# Hello World
# This is a test filetest1
# test2
# test3

 