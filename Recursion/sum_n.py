# Without Recursion
# def sum_no(n):
#     sum=0
#     i=1
#     while i<=n:
#         sum+=i
#         i+=1
#     return sum

# print(sum_no(5))   

# Time Complexity: O(n)
# Space Complexity: O(1+1) - O(2) = O(1)

# Mathematical Formula Approach
# def sum_no(n):
#     sum = (n*(n+1))/2
#     return sum

# print(sum_no(5))  

# Using recursion
# sum is used each time,so we pass sum to the function
# def x(n,sum):
#     if n!=0:
#         sum+=n # sum=2, sum=1+2=3
#         return x(n-1,sum) # x(1,2) x(0,3)
#     return sum

# print(x(2,0))  

# Time Complexity: O(N) - the operation occurs for N times.(given number value)
# Space Complexity: O(N) { In the worst case, the recursion stack space would be full with all the function calls waiting to get completed and that would make it an O(N) recursion stack space }


# # Using recursion
# Functional way
# sumOfNaturalNumbers(N) = N + sumOfNaturalNumbers(N-1);
def s(n):
    if n==0:
        return 0
    return n+s(n-1)

print(s(5)) # 5+4+3+2+1 =15