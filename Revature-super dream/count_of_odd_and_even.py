# write a program to display count of all odd and even numbers between 1 and n 

# sample input:

# 10

# output

# 5 5

n=int(input())
odd=0
even=0
for i in range(1,n+1):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(odd,end=" ")
print(even)