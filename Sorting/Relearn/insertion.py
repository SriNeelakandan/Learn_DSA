# Insertion sort
# Takes an element and place it current order 

x=list(map(int,input().split()))
n=len(x)

for i in range(1,n):
    j=i
    while j>0 and x[j]<x[j-1]:
        x[j],x[j-1]=x[j-1],x[j]
        j-=1
        print("runs")
    print("outer runs")
    # print(x)

print(f"final : {x}")

# Time Complexity: O(N^2)
# Space Complexity: O(1)

# Time Complexity can be optimised by didswap variable or using while loop, Only outer loop runs
# Time Complexity: O(N)