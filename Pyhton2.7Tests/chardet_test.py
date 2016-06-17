# coding=utf-8
import os,chardet
print os.getcwd() # 打印当前工作目录
os.chdir("C:\Users\Administrator\Desktop\Pyhton2.7Tests") # 修改当前工作目录
f = open("chardet_test.txt", "r")
result = chardet.detect(f.read()) # chardet.detect()方法返回一个字典，confidence是精确度，encoding是编码格式。
print result 
f.close()

sstr = "hello"
ustr = "hello".encode("utf-8")
print chardet.detect(sstr)
print chardet.detect(ustr)
s = "\u91d1\u5e01\u50a8\u5907"   
print s  
print chardet.detect(s)
print s.decode("unicode_escape")

import urllib2 # 测试网页编码
d = urllib2.urlopen("http://www.baidu.com") 
print chardet.detect(d.read())
            # GB2312是中国规定的汉字编码，也可以说是简体中文的字符集编码;GBK 是 GB2312的扩展 ,除了兼容GB2312外，它还能显示繁体中文，还有日文的假名
            # chardet.detect检测到的编码是GB2312，但是实际上的应该是 <meta http-equiv="Content-Type" content="text/html; charset=gbk" />
            # 网页是GBK，所以此时的精确度是99%。
# 输出
# D:\Program Files (x86)\Notepad++
# {'confidence': 1.0, 'encoding': 'ascii'}
# {'confidence': 0.99, 'encoding': 'utf-8'}
# 请按任意键继续. . .