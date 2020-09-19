import pybase64 as b64
a=b"I am a cricket player"# b is to convert into byte
c=b64.b64encode(a)
print(c)
d=b64.b64decode(c)
print(d)
