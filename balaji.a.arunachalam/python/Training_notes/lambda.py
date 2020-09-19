cube = lambda x,y:(x+y)
print(cube(3,5))
a = [(lambda x: x * 2)(x) for x in range(5)]
print(a)
a=[1,2,3,4,5,6,7,8]
a.reverse()
print(a)
#print(list(reversed(a)))
a.sort()
print(a)
print(sorted(a))