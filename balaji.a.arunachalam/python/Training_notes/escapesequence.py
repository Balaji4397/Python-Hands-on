print("line1\nline2\tline3")# r wont perform escape sequence
print("\"line1\'line2\\line3\"")
a = "1" + "\t" + "Bee"
b = "2" + r"\t" + "Tea"
print(a)
print(b)
a="cricket is the best sport"
b=a.split(" ",maxsplit=1)
b[0]="football"
#a=" ".join(b)
print(b)
c=a.rsplit(" ",maxsplit=2)#reverse split
print(c)
a = "Tea\nand coffee\rcups\n"
print(a.splitlines())
print(a.splitlines(keepends=True))
a="--cricket is the best sport--"
print(a.lstrip("--"))
a.replace("cricket","football")
print(a)
a = "Tea bag. Tea cup. Tea leaves."
print(a.replace("Tea", "Coffee"))
print(a.replace("Tea", "Coffee", 1))
x=["abc","sdf","dfg","fgh"]
y=[1000,2000,1500,3000]
for a in x:
    print("my name  %s and salary is %d" % (a,10))
print("my name is {name} and {salary}".format(name="abc",salary=1000))
a="cricket is the best sport"
b=a.split(" ")
print(" ".join(b))
c="".join(x)
print(c)
a=str.maketrans('a','1')
b="balaji"
print(b.translate(a))