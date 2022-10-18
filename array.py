from array import *
from numpy import *

# vals = array('i', [1, 3,5, 8, 9])

# newArr = array(vals.typecode, (a*a for a in vals))

# i = 0 
# while i<len(newArr):
#     print(newArr[i])
#     i+=1


# vals.reverse()
# print (vals.buffer_info())
# print(vals.typecode)

# for i in range(5):
#     print(vals[i])

# for i in range(len(vals)):
#     print(vals[i])

# for e in vals:
#     print(e)
    
# myVals = array('u', ['a','b','c','d','e',])
# for e in newArr:
#     print(e)

# ------------------------------------------------------------------------------------------------------------

# arr = array('i', [])

# n = int(input("Enter the length of the array: "))

# for i in range(n):
#     x = int(input("Enter the next value: "))
#     arr.append(x)
    
    
# print(arr)

# val = int(input("Enter the value for search: "))

# k = 0
# for e in arr:
#     if e==val:
#         print(k)
#         break
#     else: print("invalid input")
#     k+=1
    
#------------------------------------------------------------------------ 
# arr = array([1,2,3,2,3,4])

# print(arr)

#----------------------------------------------------------------------------------------------------------

arr1 = array([1,2,3,2,3,4])
# arr2 = array([10,3,6,9,5,8])
# arr2 = arr1.view()
arr2 = arr1.copy()

# print(sin(arr1))
# print(cos(arr1))
# print(log(arr1))
# print(sqrt(arr1))
# print(sum(arr1))
# print(min(arr1))
# print(max(arr1))
# print(sort(arr1))


# arr3 = arr1 + arr2
# print(arr3)

print(concatenate([arr1, arr2]))
print(id(arr1))
print(id(arr2))

