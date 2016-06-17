# coding=utf-8

def staticm():
    print "staticm"

class a():
    @staticmethod
    def staticm2():
        print "staticm2"
        
    def normalm(self):
        print "normalm",self

    def classm(cls):
        print "class",cls
 
def main():
    staticm()
    
    a1 = a()
    a1.staticm2()
    a1.normalm()
    a1.classm()
    
if __name__ == "__main__":
    main()
    
# log:
# staticm
# staticm2
# normalm <__main__.a instance at 0x026E58A0>
# class <__main__.a instance at 0x026E58A0>