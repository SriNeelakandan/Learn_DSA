# Brute force

# def fib(n):
#     x1=0
#     x2=1
#     res=""
#     while n>=0:
#         res += str(f" {x1}")
#         x1,x2=x2,x1+x2        
#         n-=1
#     return res
# print(fib(5))

# Time Complexity : O(n)
# Space Complexity: O(n)

# Optimal

# using formula fib(i) = fib(i-1) +fib(i-2)

# def fib(n):
#     x=[0] * n
#     x[0]=0
#     x[1]=1
#     for i in range(2,n):
#         x[i]=x[i-1]+x[i-2]
#     return x

# print(fib(5))

# Another space optimized

# def fib(n):
#     x1=0
#     x2=1
#     while n>=0:
#         print(x1,end=" ")
#         x1,x2=x2,x1+x2        
#         n-=1
    
# print(fib(5))
# Time Complexity: O(n)
# Space Complexity: O(1)

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

def terms(n):
    res=[]
    for i in range(n):
        res.append(fib(i))
    return res

print(terms(5))


# Step 1: Understand the recursive function

# For each call fibonacci(N):

# It calls fibonacci(N-1) and fibonacci(N-2).

# Each of those again calls two more functions… and so on.

# That creates an exponential recursion tree.

# Each node calls 2 subproblems → roughly O(2^N) total function calls.
# So:

# Time Complexity of fibonacci(N) = O(2^N)

# Space Complexity: O(N) { At maximum there could be N function calls waiting in the recursion stack since we need to calculate the Nth Fibonacci number for which we also need to calculate (N-1) Fibonacci numbers before it }.

