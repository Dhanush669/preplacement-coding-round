# Write a program to find position of the third smallest number in the given array.

# Inputs first line will have no of elements n second line will have n elements separated by space

# Output- position of in array starting with 1, display -1 if not

# found in array.

# e.g.

# Input

# 4

# 22 33 11 44

# Output

# 2

n=int(input())
s=input()

arr=list(s.split(" "))
flag=True
for i in range(0,n):
    temp=arr[i]
    if temp[0]=="1":
        flag=False
        print(i)
        break
if flag:
    print("-1")