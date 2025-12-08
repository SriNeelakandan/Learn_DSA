# Bruteforce Approach
class count_digit:
    def count(self,n):
        self.count =0
        self.no=n
        while self.no>0:
            self.count+=1
            self.no =self.no//10

        return self.count
c=count_digit()
n=int(input("Enter a number: "))
print(c.count(n))



# Time Complexity: O(log10N + 1) where N is the input number. The time complexity is determined by the number of digits in the input integer N. In the worst case when N is a multiple of 10 the number of digits in N is log10N + 1.
# the loop runs for n times(n - no of digits of a number)
# What is no of digits?
# - 10^(d-1) < N < 10^d 
# here d- no of digits , N- number
# lets eg: N=25 , d=2 , 
# apply the formula:
# 10^(2-1) < 25 < 10^2 - 10 <25<100

# from this, we can say no of digits(d) as
# d=log10(N)
# for no 10, we get digit as 1
# so we add +1 
# d= log10(N)+1

# Hence , time complexity is O(log10(N)+1)

# In the while loop we divide N by 10 until it becomes 0 which takes log10N iterations.
# In each iteration of the while loop we perform constant time operations like division and increment the counter.
# Space Complexity : O(1) as only a constant amount of additional memory for the counter regardless of size of the input number.

#--------------------------------------------------------------------------
# Optimal Approach

import math
class solution:
    def find_count(self,n):
        self.cnt = int(math.log10(n) + 1)
        return self.cnt
s=solution()
print(s.find_count(1243))

# Time Complexity: O(1)as simple arithmetic operations in constant time are computed on integers.

# Space Complexity : O(1)as only a constant amount of additional memory for the count variable regardless of size of the input number.