# write a program to find the position of first 2 consecutive repeated characters in a string

# position starting with 1, display -1 if not fount.

# sample input:

# abcdder

# output:

# 4

s=input()
position=0
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        position=i+1
        break
if position==0:
    print(-1)
else:
    print(position)