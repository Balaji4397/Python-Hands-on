
student1={"Name":'Balaji',"age":24,"Gender":'Male'}
print(student1['Name'])
student1['Name']="A.Balaji"
print(student1['Name'])
print(student1['age'])
student1["sport"]="Cricket"
print(student1)
del student1["age"]
print(student1)
student1.clear()
print(student1)
del student1
name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
dict = {}
for x in name:
    for y in animal:
        dict[x] = y
        animal.remove(y)
        break
print("result dictionary is:" + str(dict))
s={}
print(s)
s={'name':'balaji','age':23,'gender':'Male'}
print(s.keys())
print(s.values())
s['age']=23
print(s)
print(s.get("gender"))
for x,y in s.items():
    print(x,y)
for x in s:
    print(x)
for x in s:
    print(s[x])
print('name' in s)
s['sport']="cricket"
print(s)
s.pop('sport')
print(s)
s={'name':'balaji','age':23,'gender':'Male'}
t=s.copy()
print(t)
r={}
r=s
print(r)
s["age"]=24
print(s)
print(r)
print(t)
a={'name':'abc','gender':'male'}
a=dict(c=50,d='hello')
print(a.setdefault('d','gh'))
a=[1,2,3,4]
print(a[::-1])

