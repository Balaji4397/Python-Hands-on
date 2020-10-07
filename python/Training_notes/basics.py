
a=10
print(a)
a="India"
print(a)
def sample():
    global a
    print(a)
    a=20
    print(a)

sample()
print(a)
a,b,c=5,"Sample",6.5
print(a,b,c)
s=5+3
print(s)
b='5'+'3'
print(type(s))#printing s
"""Hi"""
_a=10
print(_a)
a=0xA0F
print(a)
'''
a="Hello World"
print(a.istitle())
b=['football','cricket']
c=b
d=['football','cricket']
e="Hello World"
print(c==b)
print(c is b)
print(d==b)
print(d is b)
print(id(a),id(b),id(c),id(d),id(e))
print(a.find('W'))
print(a.count('o'))
print(a.capitalize())
name="balaji"
age=24
str=f'Hi my name is {name}, I am {age} years old'
print(str)
print(str.index('am',3,10))
str1='Hi my name is {}, I am {} years old'.format(name,age)
print(str1)
print("".join(reversed(str)))
import  pybase64 as b64
b=b"India"
c=b64.b64encode(b)
a=f"password:{c}"
print(a)
d=b64.b64decode(c)
a=f"password:{d}"
print(a)
a="I am a cricket player and I am a opener"
print(a.partition("and"))'''
