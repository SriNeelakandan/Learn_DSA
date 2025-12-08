# Bruteforce

# def check(x,n):
#     p1= 0
#     p2=n-1
#     while p1<p2:
#         if x[p1] == x[p2]:
#             p1+=1
#             p2-=1
#         else:
#             return False
#     return True
# name ="TAKE U FORWARD"
# l=len(name)
# if check(name,l):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Time complexity: O(N)
# Space Complexity: O(1)

# Using Recursion
def check(x,p1,p2):
    if p1<p2:
        if x[p1] == x[p2]:
            p1+=1
            p2-=1
            return check(x,p1,p2)
        else:
            return False
    return True
name ="neels"
l=len(name)
if check(name,0,l-1):
    print("Palindrome")
else:
    print("Not Palindrome")

# Time Complexity: O(N)
# Space Complexity: O(1)