#Reverse a List without using inbuilt function

def lst_rev(nums):
    #nums=[1,2,3,4,5]
    #print(nums[::-1]) using slicing concept
        a=int(len(nums))
        for x in range(int(a/2)):
            temp=nums[x]
            nums[x]=nums[a-x-1]
            nums[a-x-1]=temp
        return nums

#To bring 0 to the starting of the list

def StartZero(a):
    #a=[1,0,5,0,3]
    count=0
    for x in a:
        if x==0:
            count+=1
            a.remove(0)
    while count!=0:
        a.insert(0,0)
        count-=1
    return a

#Give two list, merge them as below
#nums1 = [1,3,5] ; nums2 = [2,4,6]
#Output:
#nums = [1,2,3,4,5,6]

def merge(a,b):
    num=a+b
    num.sort()
    return num
#num1,num2,num=[1,3,5],[2,4,6],[]
#result=merge(num1,num2)
#print(result)

#Wrte a function to reverse cases:
#str = "aBCDwd" output= "AbcdWD"

def abc(str):
    b=""
    for x in range(len(str)):
        a=ord(str[x])
        if a>=97 and a<=122:
            a-=32
            b+=chr(a)
        elif a>=65 and a<=90:
            a+=32
            b+=chr(a)
        else:
            b+=str[x]
    return b
#str="aBGtu"
#c=abc(str)
#print(c)

#Arrange odd numbers in left part of list and even numbers to right part of list
#nums = [1,2,6,3,5,7]

#without using more memory consuption
def oddeven_1(nums):
    count=0
    b=len(nums)
    while b>0:
        if nums[count]%2 !=0:
            count+=1
            b-=1
        else:
            a=nums[count]
            nums.pop(count)
            nums.append(a)
            b-=1
    return nums
#nums=[1,2,6,3,4,7]
#output=oddeven(nums)
#print(output)

#with using more memory consumption
def oddeven_2(nums):
    odd,even=[],[]
    b=len(nums)
    for x in nums:
        if x%2 !=0:
            odd.append(x)
        else:
            even.append(x)
    return odd+even
# nums=[-1,2,6,3,4,7]
# output=oddeven_2(nums)
# print(output)

#Given a list, find max increasing sum continous array, and return subarray(continous)
#nums =[1,2,0,2,3,4,-1,2,4,5,7,8]

def sum(lst):
    a,count=0,0
    lst1,temp,lst2=[],[],[]
    for x in lst:
        if x>0:
            a+=x
            temp.append(x)
        else:
            lst1.append(a)
            a=0
            lst2.append(temp)
            temp=[]
    lst2.append(temp)
    lst1.append(a)
    m=max(lst1)
    index=lst1.index(m)
    return lst2[index]
#nums =[1,2,0,2,3,4,-1,2,4,5,7,8]
# output=sum(nums)
# print(output)

#Given a list, order the list with 0's at the end
#nums =[1,2,0,3,4,0,0,7,8,0,2]

def order(a):
    b=[]
    for x in range(len(a)):
        if a[x]==0:
            b.append(x)
            a.insert(len(a)+1,0)
    for x in range(len(b)):
        a.pop(b[x]-x)
    return a
#nums =[1,2,0,3,4,0,0,7,8,0,2]
#output=order(nums)
#print(output)

#Given list of numbers, find if m elements are repeated k times(continous)
#nums = [1,2,3,4,4,4,4] m = 1 k = 3
#output : True
#nums = [1,2,3,7,2,4,4,4] m = 2 k = 2
#output : False
#nums = [1,2,3,3,2,1,4,4,4] m = 3 k = 2
#output : True

# def repeat_1(nums,m,k):
#     count=0
#     for x in range(len(nums)-(k-1)):
#         if k==3:
#             if ((nums[x+1]-nums[x]==1  and nums[x+2]-nums[x+1]==1)) or ((nums[x+1]-nums[x]==-1  and nums[x+2]-nums[x+1]==-1)):
#                 #print(nums[x:k+x] or nums[x:k+x][::-1])
#                 count+=1
#                 if count>=k:
#                     return True
#         else:
#             if (nums[x+1]-nums[x]==1) or (nums[x+1]-nums[x]==-1):
#                 #print(nums[x:k+x] or nums[x:k+x][::-1])
#                 count+=1
#                 if count>=k:
#                     return True
#     if count<m:
#         return False
# nums = [1,2,3,4,4,4,3]
# m = 1
# k = 3
# output=repeat_1(nums,m,k)
# print(output)

def repeat_2(nums,m,k):
    count=1
    prev_value=0
    for x in range(len(nums)-m):
        if x>0 and (nums[x:m+x]==prev_value or nums[x:m+x][::-1]== prev_value):
            count+=1
            if count>=k:
                return True
        else:
            prev_value = (nums[x:m + x])
    if count<k:
        return False
# nums = [1,2,3,4,4,4,4]
# m = 1
# k = 3
# output=repeat(nums,m,k)
# print(output)
# nums = [1,2,3,7,2,4,4,4]
# m = 2
# k = 2
# output=repeat(nums,m,k)
# print(output)
# nums = [1,2,3,3,2,1,4,4,4]
# m = 3
# k = 2
# output=repeat(nums,m,k)
# print(output)











