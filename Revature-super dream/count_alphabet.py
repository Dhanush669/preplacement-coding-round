# write a program to count word ending with alphabet "a" in given string

# sample input:

# an apple in a basket

# output:

# 1

s=input()
arr=list(s.split(" "))
count=0
for i in arr:
    if i[-1]=="a":
        count=count+1
print(count)