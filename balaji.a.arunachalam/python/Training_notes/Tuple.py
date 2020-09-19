'''
a=1,2,3,4,5
print(a)
print(a[0:2])
print(a[-1])
#a.reverse() is not possible
#append is not possible in tuple eg:a[1]=10
del a
#print(a)
#remaining all same as list
b=[6,7,8,9]
tuple(b)#converting list to tuples
print(b)
print(min(b))
print(max(b))
c=(1,2,3,4)
print(c)'''
a=(1,2,3,4,5)
print(a)
c=(6,7)
print(c)
b=(6,)
print(type(b))
print(a[1:3])
a=(1,2,3,2,5)
print(a.count(2))
print(a)
print(6 not in a)
print(a[3])
for x in a:
    print(x)
c=a+b
print(c*3)
print(c[2])
a=(1,2,[3,4,5],6)
print(a[2][0])
a[2][0]=7
print(a)
a=(1,2,3,4)
b,c,d,e=a#unpacking tuple
print(c)
print(a[3])
a=('b','a','l','a','j','i')
a=''.join(a)#tuple to string
print(a)
a=(1,2,3,2,4,3,4)
print(a.count(4))
b=list(a)
b.remove(3)
print(b)
a=((1,2),(3,4),(5,6))
print(list(zip(*a)))
a=[10,20,50,(1,2,3),30,40]
c=0
for x in a:
    if isinstance(x,tuple):
        break
    c+=1
print(c)

