# -*- coding: UTF-8 -*-
# 1.区别：
# (1)str和unicode都是basestring的子类
sstr = "hello"   #str
ustr = u"hello"  #unicode
print isinstance(sstr, basestring)
print isinstance(ustr, basestring)

# (2)str是字节串，由unicode经过编码(encode)后的字节组成的;unicode是真正意义上的字符串，由字符组成
sstr = "hello world" 
sstr = u"hello world".encode("utf-8")
print len(sstr)  #11
# 返回字节数  str = "中文"  为'\xe4\xb8\xad\xe6\x96\x87'
ustr = u"hello world"
ustr = "hello world".decode("utf-8")
ustr = unicode("hello world", "utf-8")
print len(ustr)  #11
# 返回字节数   ustr = u"中文"  为u'\u4e2d\u6587'

# 2.转化：unicode2str  str2unicode
# (1)unicode to str "encode" 编码
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
# (2)str to unicode："decode" 解码
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
# 3.区分方法：
print isinstance(u"hello world", unicode)
print isinstance("hello world", str)
# 4.不同编码转换,使用unicode作为中间编码
print type(unicode(asciistring, "ascii").encode("utf-8"))
print type(plainstring3.decode("ascii").encode("utf-8"))
# 5.python文件编码：头文件首行添加# -*- coding: utf-8 -*- 或者 #coding=utf-8 
# 6.文件编码检测
import os,chardet
print os.getcwd();
os.chdir("C:\Users\Administrator\Desktop\Pyhton2.7Tests") 
f = open("chardet_test.txt","r") 
result = chardet.detect(f.read()) # {"confidence": 0.99, "encoding": "utf-8"} 
print result 
# 7. \u字符串转对应unicode字符串
# u"中" u"\u4e2d"  
s = "\u4e2d" 
print s
print s.decode("unicode_escape") #中  unicode_escape:转义unicode字符串
a = "\\u4fee\\u6539\\u8282\\u70b9\\u72b6\\u6001\\u6210\\u529f" 
print a
print a.decode("unicode_escape") 
# 8. 文件处理,IDE和控制台
# 读文件  外部输入编码，decode转成unicode  处理(内部编码，统一unicode)  encode转成需要的目标编码  写到目标输出(文件或控制台) 
# 结论：搞明白要处理的是str还是unicode, 使用对的处理方法(str.decode/unicode.encode)

sstr = "this is string example....wow!!!";
sstr = sstr.encode('base64','strict');
print "Eencoded String: " + sstr
print "Decoded String: " + sstr.decode('base64','strict')
#输出
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
# 中
# \u4fee\u6539\u8282\u70b9\u72b6\u6001\u6210\u529f
# 修改节点状态成功
# Eencoded String: dGhpcyBpcyBzdHJpbmcgZXhhbXBsZS4uLi53b3chISE=

# Decoded String: this is string example....wow!!!
# 请按任意键继续. . .
