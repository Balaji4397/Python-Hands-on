'''class sample1:
    def __init__(student,name,age):
        student.name=name
        student.age=age
    x=5
class sample2:
    x=15
object1=sample1('abc',25)
object2=sample1('bcd',24)
object2=sample1('cde',25)
print(sample1.x)
print(sample2.x)'''
'''class sample_class:
    def __init__(self,a,b):
        self.c=a
        self.d=b
    def fun1(self):
        s="Hi,Hello"
        return s
p1=sample_class(10,50)
p2=sample_class(5,10)
print(p1.fun1())
class sample_class2(sample_class):
    def __init__(self,a,b):
        self.c=a
        self.d=b
    print(p1.c,p1.d)
p3 = sample_class(2, 3)
print(p3.c)
print(p3.d)'''
'''class sample:
    def __init__(self,a,b):
        self.c = a
        self.d = b
        print(self.c,self.d)
d = sample(5,6)
f = sample(6,6)
class sample2(sample):
    pass
g = sample2(8,9)
class sample3(sample):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.f = c
        #self.d = b
        #print(self.f,self.a,self.b)
n = sample3(9,4,3)
print(n.f,n.c,n.d)'''
class sample1:
    def __init__(self,a,b):
        self.c = a
        self.d = b
        print(self.c,self.d)
d = sample1(5,6)
f = sample1(6,6)
class sample2():
    def __init__(self,a,b):
        self.e = a
        self.f = b
        print(self.e,self.f)
g = sample2(8,9)
class sample3(sample1,sample2):#multiple inherit
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.g = c
n=sample3(5,6,7)
print(n.g,n.c,n.d,n.e,n.f)