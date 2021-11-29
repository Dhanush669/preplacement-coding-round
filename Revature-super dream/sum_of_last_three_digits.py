# Write a program to find the sum of last three digits of a given

# number

# e.g.

# Input 2345

# Output

# 12

n=int(input())
ans=0
for i in range(0,3):
    temp=n%10
    ans=ans+temp
    n=n//10
print(ans)