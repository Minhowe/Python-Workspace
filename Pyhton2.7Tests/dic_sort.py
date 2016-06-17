# encoding=utf-8
def sortedDictValues(dic, reverse=False):
    keys = dic.keys()
    keys.sort(reverse = reverse)
    return [dic[key] for key in keys]

def sortedDictKeysValues(dic, reverse=False):
    keys = dic.keys()
    keys.sort(reverse = reverse)
    return [(key,dic[key]) for key in keys]
        
def sorted_dic(container,keys,reverse):
    # return keys list base on  equivalent value of container 
    print container
    print keys
    aux = [(container[k],k) for k in keys]
    print aux
    aux.sort()
    if reverse:aux.reverse()
    return [k for v,k in aux]
    
    
if __name__ == '__main__':
    dic =  {'c':1,'e':'5','b':7}
    print dic
    print sortedDictValues(dic, False)
    print sortedDictValues(dic, True)
    print sortedDictKeysValues(dic, False)
    print sortedDictKeysValues(dic, True)

    
    for key in dic.keys():
        print key
    
    keys = dic.keys()
    
    dic =  {1:1,2:2,3:3}
    container = [1,2,3]
   
    print sorted_dic(container, dic.keys, False)
    

    # print [(container[k],k) for k in keys]
    # print [(container[k],k) for k in keys]