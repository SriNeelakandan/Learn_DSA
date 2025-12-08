# #Brute Force Approach

# class solution:
#     def print_divisors(self,n):
#         self.divisor=[]
#         for i in range(1,n+1):
#             if n % i ==0:
#                 self.divisor.append(i)
#         return self.divisor

# n=int(input("Enter a number: "))
# s=solution()
# print(s.print_divisors(n))

# # Time Complexity:
# # O(N), we check for every number from 1 to N.
# # O(N), extra space used for storing divisors.

# Optimal approach
import math
class solution:
    def print_divisors(self,n):
        self.divisor=[]
        for i in range(1,int(math.sqrt(n))+1):
            if n % i ==0:
                self.divisor.append(i)
            if i != n//i:
                self.divisor.append(n//i)
        return self.divisor
n=int(input("Enter a number: "))
s=solution()
print(s.print_divisors(n))

# Time Complexity: O(sqrt(N)), we check for every number between 1 and sqaure root of N.
# Space Complexity: O(2*sqrt(N)), extra space used for storing divisors.