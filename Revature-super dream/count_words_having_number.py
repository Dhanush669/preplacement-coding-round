# write a program to count words having number in a string.

# sample input:

# abc1 def ghi2 jkl3

# output:

# 3

s=input()
count=0
lis=s.split()
alp=False
num=False
for i in lis:
    alp=0
    num=0
    for j in i:
        if j.isnumeric():
            num=True
        elif j.isalpha():
            alp=True
           
    if alp and num:
        count+=1
        
print(count)

