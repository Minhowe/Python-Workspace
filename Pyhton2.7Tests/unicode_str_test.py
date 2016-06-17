# -*- coding: UTF-8 -*-
# 1.����
# (1)str��unicode����basestring������
sstr = "hello"   #str
ustr = u"hello"  #unicode
print isinstance(sstr, basestring)
print isinstance(ustr, basestring)

# (2)str���ֽڴ�����unicode��������(encode)����ֽ���ɵ�;unicode�����������ϵ��ַ��������ַ����
sstr = "hello world" 
sstr = u"hello world".encode("utf-8")
print len(sstr)  #11
# �����ֽ���  str = "����"  Ϊ'\xe4\xb8\xad\xe6\x96\x87'
ustr = u"hello world"
ustr = "hello world".decode("utf-8")
ustr = unicode("hello world", "utf-8")
print len(ustr)  #11
# �����ֽ���   ustr = u"����"  Ϊu'\u4e2d\u6587'

# 2.ת����unicode2str  str2unicode
# (1)unicode to str "encode" ����
unicodestring = u"Hello world"
utf8string = unicodestring.encode("utf-8") 
print type(utf8string)
print utf8string
asciistring = unicodestring.encode("ascii")
print type(asciistring)
print asciistring
isostring = unicodestring.encode("ISO-8859-1")
print type(isostring)
print isostring
utf16string = unicodestring.encode("utf-16")
print type(utf16string)
print utf16string
# (2)str to unicode��"decode" ����
plainstring1 = utf8string.decode("utf-8")
print type(plainstring1)
print plainstring1
plainstring1 = unicode(utf8string, "utf-8")
print type(plainstring1) 
print plainstring1
plainstring2 = asciistring.decode("ascii")
print type(plainstring2) 
print plainstring2
plainstring3 = isostring.decode("ISO-8859-1")
print type(plainstring3) 
print plainstring3
plainstring4 = utf16string.decode("utf-16")
print type(plainstring4) 
print plainstring4
assert plainstring1 == plainstring2 == plainstring3 == plainstring4 
# 3.���ַ�����
print isinstance(u"hello world", unicode)
print isinstance("hello world", str)
# 4.��ͬ����ת��,ʹ��unicode��Ϊ�м����
print type(unicode(asciistring, "ascii").encode("utf-8"))
print type(plainstring3.decode("ascii").encode("utf-8"))
# 5.python�ļ����룺ͷ�ļ��������# -*- coding: utf-8 -*- ���� #coding=utf-8 
# 6.�ļ�������
import os,chardet
print os.getcwd();
os.chdir("C:\Users\Administrator\Desktop\Pyhton2.7Tests") 
f = open("chardet_test.txt","r") 
result = chardet.detect(f.read()) # {"confidence": 0.99, "encoding": "utf-8"} 
print result 
# 7. \u�ַ���ת��Ӧunicode�ַ���
# u"��" u"\u4e2d"  
s = "\u4e2d" 
print s
print s.decode("unicode_escape") #��  unicode_escape:ת��unicode�ַ���
a = "\\u4fee\\u6539\\u8282\\u70b9\\u72b6\\u6001\\u6210\\u529f" 
print a
print a.decode("unicode_escape") 
# 8. �ļ�����,IDE�Ϳ���̨
# ���ļ�  �ⲿ������룬decodeת��unicode  ����(�ڲ����룬ͳһunicode)  encodeת����Ҫ��Ŀ�����  д��Ŀ�����(�ļ������̨) 
# ���ۣ�������Ҫ�������str����unicode, ʹ�öԵĴ�����(str.decode/unicode.encode)

sstr = "this is string example....wow!!!";
sstr = sstr.encode('base64','strict');
print "Eencoded String: " + sstr
print "Decoded String: " + sstr.decode('base64','strict')
#���
# True
# True
# 11
# 11
# <type 'str'>
# <type 'str'>
# <type 'str'>
# <type 'str'>
# <type 'unicode'>
# <type 'unicode'>
# <type 'unicode'>
# <type 'unicode'>
# <type 'unicode'>
# True
# True
# <type 'str'>
# <type 'str'>
# D:\Program Files (x86)\Notepad++
# {'confidence': 1.0, 'encoding': 'ascii'}
# \u4e2d
# ��
# \u4fee\u6539\u8282\u70b9\u72b6\u6001\u6210\u529f
# �޸Ľڵ�״̬�ɹ�
# Eencoded String: dGhpcyBpcyBzdHJpbmcgZXhhbXBsZS4uLi53b3chISE=

# Decoded String: this is string example....wow!!!
# �밴���������. . .
