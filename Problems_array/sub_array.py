# No of Sub arrays of size 3 with some condition

# class solution:
#     def countsubarrays(self,nums,n):
#         ans=0
#         for i in range(0,n-2):
#             if nums[i+1]== (nums[i]+nums[i+2]):
#                 ans+=1
#         return ans
    
# s=solution()
# x=[1,2,1,3,5,2,4,2]
# print(s.countsubarrays(x,len(x)))

# # maximum no of people

# class solution:
#     def maximumPeople(self,n,x,w):
#         count=0
#         sum=0
#         x.sort()
#         for i in x:
#             if sum+i<=w:
#                 sum+=i
#                 count+=1
#             else:
#                 break
#         return count
    
# s=solution()
# # x=[4,3,5,1,1,2]
# n=int(input())
# x=list(map(int,input().split()))
# w=int(input())
# print(s.maximumPeople(n,x,w))


# return maximum permutation count of string elements
# by removing vowels,if no consonants return 0

# class Solution:
#     def fact(self,x):
#         if x== 0 or x==1:
#             return x
#         else:
#             return x*Solution.fact(self,x-1)
    
#     def maxPermutation(self,arr):
#         vowels="aeiouAEIOU"
#         res=""
#         maximum=0
#         for i in arr:
#             sum=0
#             for a in i:
#                 if a not in vowels:
#                     sum+=1
#             if sum>maximum:
#                 maximum =sum
#                 res=i
#         if maximum==0:
#             return 0
#         return  res,Solution.fact(self,maximum)

# s=Solution()
# # x={"aaeiou","aaeiou","aaeiou"}
# x=list(input().split())
# # x=['ccbc' ,'hello' ,'aaeiou']
# print(s.maxPermutation(x))

# class Solution:
#     def display(self,arr,n):
#         for i in arr:
#             print(f"{i}-{chr(i)}")
#         return 0

# s=Solution()
# x=list(map(int,input().split()))
# n=int(input())
# s.display(x,n)

# class Solution:
#     def numerology(self,name,n):
#         sum=0
#         product=1
#         for i in range(n):
#             product=ord(name[i]) * (i+1)
#             if ((i+1)%2 !=0) or (ord(name[i])%2 !=0):
#                 sum+=product
#         return sum
    
# s=Solution()
# n=int(input())
# names=input()
# print(s.numerology(names,n))

# Minimum Operation needed for 
# making list of size N to
# contains element - 1 to N

# class solution:
#     def minimumoperation(self,arr,n):
#         arr.sort()
#         res=0
#         for i in range(0,n):
#             if arr[i]<i+1:
#                 res+= ((i+1)-arr[i])
#                 arr[i]+=1
#         return res,arr
        
# s = solution()
# x=[2,4,1,1,4]
# print(s.minimumoperation(x,len(x)))

# If sum of first half of array
# less than second half of array
# reverse the array and print it

# class solution:
#     def rev(self,arr,n):
#         first_half=sum(arr[:n//2])
#         second_half=sum(arr[n//2:])
#         if first_half<second_half:
#             arr.reverse()
#         print(arr)
# s = solution()
# x=[1,2,3,10,20,30]
# print(s.rev(x,len(x)))

# Book fine:

def bookfine(d1,m1,y1,d2,m2,y2):
    if y1==y2:
        if m1==m2:
            if d1<=d2:
                return 0
            else:
                return 15 * abs(d1-d2)
        else:
            return 500 * abs(m1 - m2)
    else:
        return 10000
        
d1, m1, y1 = 14, 10, 2018
d2, m2, y2 = 5, 7, 2018
print(bookfine(d1,m1,y1,d2,m2,y2))