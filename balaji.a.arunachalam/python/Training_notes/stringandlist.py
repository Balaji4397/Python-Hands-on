'''
#first question
donut=int(input('Enter no. of donuts: '))
if donut < 10:
    print("Number of donuts: "+str(donut))
else:
    print("Number of donuts: many")
'''
'''
#second question
a=input('Enter the string: ')
b=len(a)
s=a[0:2]
d=a[-2:]
if b <= 3:
    print("")
else:
    print(s+d)
'''
'''
#third question
c=input()
d=c[0]
s=c[1:]
fix=s.replace(d,"*")
print(d+fix)
'''
'''
#fourth question
a="googleing"
b=len(a)
x=-3
y="ing"

if b<=3:
    print(a)
else:
  z = a[-3:]
  if y == z:
    a+="ly"
    print(a)
  else:
    a+=y
    print(a)
'''
'''
#fifth question
a=["apple","banana","A","sms","dood","mom"]
d,e=0,0
for x in a:
    c=len(x)
    if c>=2:
        d+=1
print("No of str len greater than 2: ",d)
for x in a:
    z=list(x)
    if len(x)>=2 and z[0]==z[-1]:
        e+=1
print("No of str with same start and end: ",e)
'''
'''
#sixth question
a=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
b,c=[],[]
for x in a:
    if x.startswith("x"):
        b.append(x)
    else:
        c.append(x)
d=sorted(b)+sorted(c)
print(d)
'''
'''
#seventh question
def duplicate(x):
    return list(dict.fromkeys(x))
a=duplicate([1,2,2,3])
print(a)

b=[1,2,3,3,2]
c=[]
for x in b:
    if x not in c:
        c.append(x)
print(c)
'''
'''
#eighth question
a=[1,2,3,4,5,6,7]
b=[]
for x in a:
    b.append(x**2)
print(b)
'''
'''
#ninth question
a=[1,2,3,4]
b=[100,200,300,400]
b.reverse()
y=0
for x in a:
        print(x,b[y])
        y+=1
'''
'''
#tenth question
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2=[]
for x in list1:
    if x !="":
        list2.append(x)
print(list2)
list3=list(filter(None,list1))
print(list3)
'''
'''
#11th question
str = "pynative"
str1=""
y=0
for x in str:
    y+=1
    if (y%2)!=0:
        str1+=x
print(str1)
str=input()
print(str[::2])
str=input()
for index in range(len(str)):
    if index % 2 == 0:
        print(str[index])
'''
'''
#12th question
list=[10,20,30,40,50]
a=list[0]
b=list[-1]
if a==b:
    print("True")
else:
    print("False")
'''
'''
#13th question
list=[10,20,33,40,17]
list1=[]
for x in list:
    if (x%5)==0:
        list1.append(x)
print(list1)
'''
'''
#14th question
s1 = "Ault"
s2 = "Kelly"
list1=list(s1)
list2=list(s2)
a=int(len(s1)/2)
s3=s1[:a]+s2+s1[a:]
print(s3)
'''
'''
#15th question
str1 = "P@#yn26at^&i5ve"
a,b,c,d=0,0,0,0
for i in range(len(str1)):
    if str1[i].isupper():
        a+=1
    elif str1[i].islower():
        b+=1
    elif str1[i].isdigit():
        c+=1
    else:
        d+=1
print("No of capital letter: ",a)
print("No of lower letter: ",b)
print("No of  digit: ",c)
print("No of special character: ",d)
'''
a = ["been", "was", "mot", "ants"]
a.sort(key=len)
#print(a)
b=[1,2,0,3]
a.sort(key=len)
print(a)
b=a.copy()
print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,11,2)))
for x in range(len(a)):
    print(x)
#a.clear()
print(a)
a.append("hello")
print(a)
a.extend(b)
print(a)

