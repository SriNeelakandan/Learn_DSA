# Bruteforce without hashing

def freq(x,n,val):
    cnt=0
    for i in range(n):
        if x[i]==val:
            cnt+=1
    return cnt

n=int(input())
arr=list(map(int,input().split()))
q=int(input())
for i in range(q):
    x=int(input())
    print(freq(arr,n,x))

# Time Complexity: N*O(N) - for each element
# Space Complexity: O(1)