# Using Hashing
# Assume that my input contains only lowercase
# a to z 
# x='a'
# print(ord(x)-ord('a'))

# Input String - 'abcdabefc'

s=input() # input string
q=int(input()) # Query count
n=len(s)

# Precomputing:
Hash_Array =[0]*26 # 0,1,--25
for i in range(n):
    Hash_Array[ord(s[i])-ord('a')]+=1

# Fetching
for i in range(q):
    x=input()
    print(Hash_Array[ord(x)-ord('a')])