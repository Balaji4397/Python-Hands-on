x=0
while x<=10:
    print(x)
    x+=1
for x in range(1,6):
    for y in range(1,x+1):
        print(y,end=' ')
    print("")
a=[10,20,30,40,50]
b=len(a)-1
for x in range(b,-1,-1):
    print(a[x])
