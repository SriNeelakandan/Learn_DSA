# Input String - 'abGcdaHbefABGc'

s=input() # input string
q=int(input()) # Query count
n=len(s)
# Hash Array size = 256
# Precomputing:
Hash_Array =[0]*255 # 0,1,--255
for i in range(n):
    Hash_Array[ord(s[i])]+=1

# Fetching
for i in range(q):
    x=input()
    print(f"{x}: {Hash_Array[ord(x)]}")