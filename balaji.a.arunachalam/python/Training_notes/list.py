
#List exercise
a=[1,2,3,4,5]
print(a)
b=[]
b.append(3)
b[0]=5
b.append(6)
b.insert(0,8)#inserting
print(b)
print(a[-2])
print(a[0:2])
print(a[4])
a[3]="append"
print(a)
del a[3]#deleting
print(a)
b=[6,7,8,9]
print(a+b)#concordination
if 3 in a:#conditions
    print("present")
x=3
for x in a:
    print(a[x])
    break
b.reverse()
print(b)
print(len(b))
d=[1,"Hello",3,7,8.5,9]
print(d[2:4])
print(len(d))
print(d*3)
c=[]
d.remove("Hello")
c=b
print(d)
x=[1,2,3,4,5]
x.pop(2)
print(x)
x=[1,"Hello",5,8,4]
#del x[2]
print(x)
#print(max(x))
#print(min(x))
#x.sort()
#x.reverse()
print(x)
y=x.index("Hello")
print(y)
z="India"
s=list(z)
print(s)
d=["apple","orange","banana"]
if "apple" in d:
    print("Present")
for x in d:
    print(x)
    if x=="orange":
        break
    else:
        print(x)
a=[1,2]
b=[1,2]
if 1 in a and 3 in b:
    print("True")

a="Hello world"
b=a.split("o")
print(b)
c="o".join(b)
print(c)
for x in a:
    print(x)
a=5
print(type(a))
b=str(a)
print(type(b))
a=['a','b','c']
b=[90,60,80]
c=['maths','science','tamil']
z=zip(a,b,c)#zippig no of list
print(z)
#f=set(z)
#print(f)
for a,b,c in z:
    print("%s scored %s in %s" % (a,b,c))

a=['a','b','c']
b=[1,2,3]
for idx,val in enumerate(a):#enumerate function
    print("%s : %s" % (idx,val))
print(a+b)
a.extend(b)
print(a)
'''
'''
a=[1,2,-4,5,-3,-2,6]
def num(x):
    if x>=0:
        return x
for b in filter(num,a):
    print(b)

def fun(x,y):
    return x+y
print(fun(3,5))
print(fun(10,50))

a=1
b=2
def add(n=2,m=3):
    return n+m
print(add(6,11))
def add(*args):
    for x in args:
        print(x)
add(5,6,7,8)
def add(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
add(a=2,b=3,c=4)
'''
'''
from functools import reduce as r#reduce function
def sub(x,y):
    return x+y
b=[100,10,5,4,6,5,10]
print(r(sub,b))
print(list(set(b)))#removing duplicates in list but unordered
print(list(dict.fromkeys(b)))#removing duplicates but in order sequence
y=0
for x in b:
    y+=x
print(y)
def mul(x):
    return x*5
c=[]
for a in map(mul,b):#map function
    c.append(a)
print(c)
a="cricket is the best sport"
from collections import Counter as count#Counter function
b=a.split(" ")
print(count(a))
print(count(b))
c=[]
a=[[1,2],[2,3],[3,4],[4,5]]
for i in a:
    c.append(i[1])
print(c)
a=[1,5,3]
b=[2,4,6]
print(any(i%2==0 for i in a))#any function
print(all(i%2==0 for i in b))#all function
a=[1,2,3,4,5,6,7,8]
a.reverse()
print(a)
print(list(reversed(a)))#difference between reverse,reversed,sort and sorted
a=[1,2,3,4]
b=[6,5,4,3]
print(list(set(a)&set(b)))#common btw two list
print(set(a)-set(b))#diff btw two lst
print(set(b)-set(a))
a=[[1,2],[2,3]]
print(list(i for x in a for i in x))#joining nested list into single list
print(a[::-1])#reverse using slicing
'''
'''
a=[1,2,0,4,3]
b=[1,2,3]
f = [ x for x in a if x>0]
print(f)
print([x+y for x in ['Python ','C '] for y in ['Language','Programming']])
a,b,c=5,7,5
if a==b:
    if a>0:
        print("True")
    else:
        print("a less than 0")
elif a==c:
    if c>0:
        print("a equal to c")
    else:
        print("c is equal to 0")
else:
    print("a not equal b and c")
'''
'''
a=10
b=0
while a>0:
    b+=a
    a-=1
    if a==9:
        continue
print(b)
def fun(a,b):
    if (a<0):
        pass
    return a+b
x=5
while x>0:
    print(fun(3,5))
    print(x)
    x+=1
    if x==10:
        break
'''
'''
a=[1,2,3]
b=[4,5,6]
for x in a:
    for y in b:
        print(x,y)

def add(a):
    return a+1
print(add(6))

a=[1,2,-4,3,-6]
def positive(x):
    if x>=0:
        return x
def negative(y):
    if y<0:
        return y
for s in filter(negative,a):
    print(s)
