'''def square(x):
    return x*x
a=[1,2,3,4,5]
x=list(map(square,a))
print(x)
from functools import reduce as r#reduce function
def sub(x,y):
    return x+y
b=[100,10,5,4,6,5,10]
print(r(sub,b))
a=[1,2,3,4,5,6]
if 7 not in a:
    raise Exception('Sorry,7 is not available')'''
a=[1,2,3,4,5]
b=iter(a)
print(b.__next__())
print(b.__next__())