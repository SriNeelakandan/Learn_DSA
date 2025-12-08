# Brute Force Approach

# n=int(input())
# def check_prime(n):
#     cnt=0
#     for i in range(1,n+1):
#         if n%i==0: 
#             cnt+=1
#     if cnt==2:
#         return True
#     return False
# print(check_prime(n))

# #Time Complexity: O(N)
# #Space Complexity: O(1)
#------------------------------------------------

# Optimal Approach
import math
n=int(input())
def check_prime(n):
    cnt=0
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: 
            return False
    return True

print(check_prime(n))

#Time Complexity: O(sqrt(N))
#Space Complexity: O(1)