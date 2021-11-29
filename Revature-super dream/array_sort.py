# Sort an array of number in ascending order

# sample input:

# 4

# 11 33 44 22

# Output
# 11 22 33 44

n=int(input())
s= input()
arr=list(s.split(" "))
arr.sort()
for i in arr:
    print(i,end=" ")