# Input : [3,1,2,1,4,3]
# Query value = [3,5,4,1,2]
# output = [2,0,1,2,1]
# Number 

# Bruteforce Approach
# def check(q,x):
#     cnt =[0] * len(q)
#     for j in range(0,len(q)):
#         for i in range(0,len(x)):
#             if q[j] == x[i]:  
#                     cnt[j]+=1
#     return cnt

# xin = [3,1,2,1,4,3]
# q_v = [3,5,4,1,2]
# print(f"Input Number: {xin}")
# print(f"Query Number : {q_v}")
# print(f"No of Occurrences: {check(q_v,xin)}")

# Time Complexity: 
# The outer loop runs for say M times (M - length of Query array)
# The inner loop runs for say N times (N - length of Input array)
# So total operations inside that loops are run for M*N times
# Hence, Time Complexity is O(M*N)

# Space Complexity: 
# The resulted occurence array of same length as Query array
# Space Complexity: O(M)

# Now, if the length of the query becomes large like 10^5 and the array size also becomes large like 10^5, the time complexity will be O(10^10).

# We know from our previous knowledge that 108 operations take 1 second to get executed. So, 1010 operations will take around 100 seconds(1010/108). We cannot say a code is good if it takes 100 seconds to get executed.

# Optimised Approach using Hashing
# hash= [0] * 12
# def precompute(x):  
#     # precompute
#     for i in range(0,len(x)):
#         hash[x[i]]+=1
#     return 0

# def fetch(n):
#     # fetch
#     return hash[n]

# xin=[3,1,2,1,4,3]
# precompute(xin)
# print(fetch(1))
# print(fetch(2))
# print(fetch(3))
# print(fetch(4))
# print(fetch(5))
#     # I assume that i create hash array of size 
#     # maximum element in input array + 1
#     # Input: [2,1,2,1,3,4] , max= 4, size =5, index {0,1,2,3,4}
#     # If maximum array element is 10^9, Can we need to create hash array of size 10^9 +1 ?
#     # No we cannot do the above
#     # The maximum size you can declare is 10^6 inside main, for global - 10^7
# # Precompute - def:
# # In this step, we will create an array(named hash array) of size 13(so that we can get the index 12) initialized with 0. In this hash array, we are going to store the frequency of each element(i.e. The number of times each element appears in the array) of the given array. To do so, we will iterate over the given array, and for each element arr[i], we will do hash[arr[i]] += 1

# # Fetching - def:
# # Fetching: In this step, we will select each query i.e. the number and for the query, we will just fetch the value of hash[number] and return it instead of running a ‘for loop’ every time. 




# # Time Complexity:  O(1) - each occurence is found at once
# # Space Complexity: O(M + 1) - M is the max element in array +1
# # Space Complexity is O(M)

# # Space Optimized Approach using Unordered Map Concept

def fn(arr,n): 
    hash_dict ={x:0 for x in arr} 

    #precompute
    for i in range(len(arr)):
        hash_dict[arr[i]]+=1

    # fetch
    return hash_dict[3]

arr = [1,2,3,1,3,2]
print(fn(arr,3))

# Final Time Complexity:(Average Case) O(N)+O(N)+O(1)= O(2N+1) ~= O(2N) ~= O(N)
# Final Time Complexity:(Worst Case) O(N^2)+O(N^2)+O(N)= O(2N^2+N) ~= O(2N^2) ~= O(N^2)
# Worstcase occurs rarely because of collisions
# Space Complexity : O(U) {U - No of unique values in given array}
