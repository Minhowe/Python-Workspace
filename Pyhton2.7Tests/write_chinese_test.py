# coding=utf-8
# how to wirite chinese to file
import os, codecs
print os.getcwd()
os.chdir("C:\Users\Administrator\Desktop\Pyhton2.7Tests")
f = codecs.open("open_file_test.txt", "a+", "utf-8")
f.write("hi")
f.write(u"你好")
f.write("你好".decode("utf-8"))
f.close()