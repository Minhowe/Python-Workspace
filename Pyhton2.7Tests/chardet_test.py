# coding=utf-8
import os,chardet
print os.getcwd() # ��ӡ��ǰ����Ŀ¼
os.chdir("C:\Users\Administrator\Desktop\Pyhton2.7Tests") # �޸ĵ�ǰ����Ŀ¼
f = open("chardet_test.txt", "r")
result = chardet.detect(f.read()) # chardet.detect()��������һ���ֵ䣬confidence�Ǿ�ȷ�ȣ�encoding�Ǳ����ʽ��
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

import urllib2 # ������ҳ����
d = urllib2.urlopen("http://www.baidu.com") 
print chardet.detect(d.read())
            # GB2312���й��涨�ĺ��ֱ��룬Ҳ����˵�Ǽ������ĵ��ַ�������;GBK �� GB2312����չ ,���˼���GB2312�⣬��������ʾ�������ģ��������ĵļ���
            # chardet.detect��⵽�ı�����GB2312������ʵ���ϵ�Ӧ���� <meta http-equiv="Content-Type" content="text/html; charset=gbk" />
            # ��ҳ��GBK�����Դ�ʱ�ľ�ȷ����99%��
# ���
# D:\Program Files (x86)\Notepad++
# {'confidence': 1.0, 'encoding': 'ascii'}
# {'confidence': 0.99, 'encoding': 'utf-8'}
# �밴���������. . .