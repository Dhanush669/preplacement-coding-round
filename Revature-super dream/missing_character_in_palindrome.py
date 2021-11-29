# write a program to find a missing character from a string(always palindrome).

# sample input:

# ab a

# output:

# b
s=input()
missingCharacter=""
posi=s.index(' ')
rev_s=s[::-1]
missingCharacter=rev_s[posi]
print(missingCharacter)