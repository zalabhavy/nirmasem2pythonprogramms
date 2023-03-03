import numpy as bhavy
arr=bhavy.array([1,2,3,4,5])
print(arr)
arr2 = bhavy.array([6,7,8,9,10])
print(arr2)
sum = arr+arr2
print("your sum is",sum)
dif = arr-arr2
print("your diffrence is",dif)
mul = arr*arr2
print("your multiplication is",mul)
div = arr/arr2
print("your division is",div)

arr = bhavy.array([[1,2],[3,4]])
print("first array is:\n",arr)
arr2 = bhavy.array([[5,6],[7,8]])
print("second array is:\n",arr2)
sum = arr + arr
print("sum is:\n",sum)
dif = arr-arr2
print("difference is\n:",dif)
mul = arr*arr2
print("multiplication is:\n",mul)
div = arr/arr2
print("division is:\n",div)

srow=s1=s2=s3=0

k = arr+arr2
print(k)
for i in range(0,2):
  srow = srow+k[0][i]
  s1 = s1 + k[0][i]
  s2 = s2 + k[1][i]
  s3 = s3 + k[i][1]

print("sum in first array's row1 elements are",srow)
print("sum in first array's row2 elements are",s1)
print("sum in fist array's column1 elements are",s2)
print("sum in fist array's column2 elements are",s3)

arr3 = bhavy.array([[1,4],[3,2]])
print(arr3)
sum = 0
even = 0
for i in range(0,2):
  for j in range(0,2):
   sum = sum + arr3[i][j]
   if arr3[i][j]%2==0:
     even = even + arr3[i][j]
  

print("your sum is:",sum) 
print("your sum of even is:",even)
print("sum of odd is:",sum-even) 

