'''
a=[1,2,3,4]
b=set()
print(b)
b=[1,2,3,5]
print(set(a)&set(b))
print(set(a)-set(b))
print(set(b)-set(a))
print(list(set(a) - set(b)))'''
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(set(sampleList))#appending two set or list and set
print(sampleSet)
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))#common item between two set
print(set1-set2)#item in set1 not in set2
print(set2-set1)#item in set2 not in set1
print(set1&set2)#common item between two set
print(set1.union(set2))# combining two set and removing the duplicate
set1.difference_update({10,20,30})#remove item from set
print(set1)
set1.update({10,20,30})
print(set1.symmetric_difference(set2))#printing all item from two set without common item
set1 = {10, 20, 30, 40, 50}
set1.remove(10)
print(set1)
set1={1,2,3}
set2={4,5,1,2,3,6,7}
print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2.isdisjoint(set1))

