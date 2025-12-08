# Bruteforce without hashing

def freq(x,n,val):
    cnt=0
    for i in range(n):
        if x[i]==val:
            cnt+=1
    return cnt

arr=input()
n=len(arr)
q=int(input())
for i in range(q):
    x=input()
    print(freq(arr,n,x))