# coding=utf-8
# delete char or str in str
sstr = "   hello"
sstr.strip()  #'\n', '\r',  '\t',  ' '
print sstr
print sstr.strip()

str1 = "123abc"
print str1.lstrip("21")
print str1.rstrip('bc')

# copy str
# strcpy(sstr1,sstr2)
sstr1 = 'strcpy'
sstr2 = sstr1
print sstr2

# cat str
# strcat(sstr1,sstr2)
sstr1 = 'strcat'
sstr2 = 'append'
sstr1 += sstr2
print sstr1

# search char
# strchr(sstr1,sstr2)
# < 0 have not finded
sstr1 = 'strchr'
sstr2 = 's'
npos = sstr1.index(sstr2)
print npos

# compare str
# strcmp(sStr1,sStr2)
sstr1 = 'strchr'
sstr2 = 'strch'
print cmp(sstr1,sstr2)

# scan str have include the char
# strspn(sstr1,sstr2)
sstr1 = '12345678'
sstr2 = '456'
# sstr1 and chars both in sstr1 and sstr2
print len(sstr1 and sstr2)

# str len
# strlen(sstr1)
sstr1 = 'strlen'
print len(sstr1)

# upper lower
# strlwr(sstr1)
sstr1 = 'JCstrlwr'
sstr1 = sstr1.upper()
print sstr1
sstr1 = sstr1.lower()
print sstr1

# cat n len str 
# strncat(sStr1,sStr2,n)
sstr1 = '12345'
sstr2 = 'abcdef'
n = 3
sstr1 += sstr2[0:n]
print sstr1

# cmp n len str
# strncmp(sstr1,sstr2,n)
sstr1 = '12345'
sstr2 = '123bc'
n = 3
print cmp(sstr1[0:n],sstr2[0:n])

# cpy n len str
# strncpy(sstr1,sstr2,n)
sstr1 = ''
sstr2 = '12345'
n = 3
sstr1 = sstr2[0:n]
print sstr1

# n char str head set 
# strnset(sstr1,ch,n)
sstr1 = '12345'
ch = 'r'
n = 3
sstr1 = n * ch + sstr1[3:]
print sstr1

# scan str
# strpbrk(sstr1,sstr2)
sstr1 = 'cekjgdklab'
sstr2 = 'gka'
npos = -1
for c in sstr1:
    if c in sstr2:
        npos = sstr1.index(c)
        break
print npos

# str rev
# strrev(sstr1)
sstr1 = 'abcdefg'
sstr1 = sstr1[::-1]
print sstr1

# find str
# strstr(sstr1,sstr2)
sstr1 = 'abcdefg'
sstr2 = 'cde'
print sstr1.find(sstr2)

# separator str
# strtok(sstr1,sstr2)
sstr1 = 'ab,cde,fgh,ijk'
sstr2 = ','
sstr1 = sstr1[sstr1.find(sstr2) + 1:]
print sstr1
# or
s = 'ab,cde,fgh,ijk'
print(s.split(','))

# join str
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)

# php addslashes 
def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)
 
s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print s
print addslashes(s)

# only char num
def only_char_num(s,oth=''):
    s2 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c,'');
    return s;
 
print(only_char_num("a000 aa-b"))

# log:
#    hello
# hello
# 3abc
# 123a
# strcpy
# strcatappend
# 0
# 1
# 3
# 6
# JCSTRLWR
# jcstrlwr
# 12345abc
# 0
# 123
# rrr45
# 2
# gfedcba
# 2
# cde,fgh,ijk
# ['ab', 'cde', 'fgh', 'ijk']
# Brazil,Russia,India,China
# John 'Johny' Doe (a.k.a. "Super Joe")\

