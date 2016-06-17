# -*- coding: UTF-8 -*-
class test1:
    pass
class test2(test1):
    pass
if __name__=="__main__":
    
    #判断类型
    a=123  #int
    print type(a)
    a=123.1 #float
    print type(a)
    a=test1() # test1
    print type(a)
    a=test2() #test2
    print type(a)
    a='string' #str
    print type(a)
    a=True #bool
    print type(a)
    a=['item'] #list
    print type(a)
    a=('item',) #tuple
    print type(a)
    a={'item':132} #dict
    print type(a)

    
    # type比较类型
    a=123  #int
    print type(a) is int
    print type(a) == int
    a=123.1 #float
    print type(a) == float
    a=test1() # test1
    b=test2() #test2
    print type(a) == type(b)
    print a == type(b) #false
    print a is type(b) #false
    print a == b       #false
    print type(a) is test1 #false
    print type(b) is test2 #false
    print type(a) is test2 #false
    print type(b) is test1 #false
    a='string' #str
    print type(a) == str
    a=True #bool
    print type(a) == bool
    a=['item'] #list
    print type(a) == list
    a=('item',) #tuple 
    print type(a) == tuple
    a={'key':132} #dict
    print type(a) == dict

    # isinstance比较类型
    a=123  #int
    print isinstance(a, int)
    a=123.1 #float
    print isinstance(a, float)

    #print isinstance(test1(), test2()) #TypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types
    print isinstance(test1(), type(test2()))
    print isinstance(test1(), test1)
    print isinstance(test2(), test2)
    print isinstance(test2(), test1)
    print isinstance(test1(), test2)  #false
    print isinstance(test2(), test1)
    a='string' #str
    print isinstance(a, str)
    a=True #bool
    print isinstance(a, bool)
    a=['item'] #list
    print isinstance(a, list)
    a=('item',) #tuple 
    print isinstance(a, tuple)
    a={'key':132} #dict
    print isinstance(a, dict)

    

    