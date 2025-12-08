# Input: [2,3,4,5,6]
# len =5,target=6,index=0
# Output : Number of Swaps required

# class Solution:
#     t_in=-1
#     def find_minimum_swaps(self,arr,n,t,i):
#         if arr[i]==t:
#             return 0
#         elif i>=n:
#             return -1
#         else:
#             for j in range(0,n):
#                 if arr[j]==t:
#                     self.t_in=j
#                     break
#             if self.t_in ==-1:
#                 return -1
#             else:
#                 return abs(self.t_in-i)
        

# # x=[2,3,4,5,7,6,9]
# x=[1,6,7,4,2]
# s=Solution() 
# print(s.find_minimum_swaps(x,len(x),2,1))

# Time Complexity: O(N)
# Space Complexity: O(1)

# Input: [1,-6,-5,-12,1,3,8,-3]
# Output: shuffle the array elements to achive maximum sum and returns the maximum sum

# Find substring of two strings
# Return the sum of ascii value of substring