def add(a,b):
    return a+b

"""
7) Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
"""
'''
nums=[1, 2, 2, 3]
result = []
for num in nums:
    if len(result) == 0 or num != result[-1]:
        result.append(num)
print(result)'''