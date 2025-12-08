# def p(n):
#     print(n,end=" ")
#     n-=1
#     if n>0:
#         p(n)
#     else:
#         return

# p(2)

# Time Complexity: O(N), we print every number from N to 1 using recursion
# Space Complexity: O(N), stack space used for recursive calls.

def p(n):
    if n==0:
        return
    
    print(n,end=" ")
    p(n-1)

p(2)