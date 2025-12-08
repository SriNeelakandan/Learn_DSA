# # Optimised Approach using Hashing 

hash = [0] * 256 
def precompute(xin):
    for x in xin:
        hash[ord(x)]+=1
    return 0

def fetch(n):
    return hash[ord(n)]

if __name__ == "__main__":
    xinp = "abNcdLaLbcNfc"
    q_v ='L'
    precompute(xinp)
    print(f" No of Occurences of {q_v} in {xinp} is {fetch(q_v)}")

# # xin = "abcdabcfc"
# # q_v ='a'

# # Declaring hash array - characters - 26(0 -25)
# # print(ord('a') - ord('a')) # 97 - 97 = 0
# # print(ord('b') - ord('a') ) # 98 -97 = 1

# def precompute(xin):
#     for x in xin:
#         hash[ord(x)]+=1
#     return 0

# def fetch(n):
#     return hash[ord(n)]

# if __name__ == "__main__":
#     xinp = "abNcdLaLbcNfc"
#     q_v ='L'
#     precompute(xinp)
#     print(f" No of Occurences of {q_v} in {xinp} is {fetch(q_v)}")

# # Time Complexity: O(1)
# # Space Complexity: O(256) - O(1)

# # hash =[0] * 26
# # For lowercase: hash[ord(x) - ord('a')] {0,1,2,3..25}
# # For uppercase: hash[ord(x) - ord('A')] {0,1,2,3...25}

# # for both
# # hash = [0] * 256
# # hash[ord(x)]

# # Space Optimized Approach using Unordered Map Concept

# def fn(arr,n): 
#     hash_dict ={x:0 for x in arr} 

#     #precompute
#     for i in range(len(arr)):
#         hash_dict[arr[i]]+=1

#     # fetch
#     return hash_dict[n]

# arr = "faxbcdbcf"
# print(fn(arr,'f'))

# Final Time Complexity:(Average Case) O(N)+O(N)+O(1)= O(2N+1) ~= O(2N) ~= O(N)
# Final Time Complexity:(Worst Case) O(N^2)+O(N^2)+O(N)= O(2N^2+N) ~= O(2N^2) ~= O(N^2)
# Worstcase occurs rarely because of collisions
# Space Complexity : O(U) {U - No of unique values in given array}
