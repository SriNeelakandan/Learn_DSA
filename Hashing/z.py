# In Number hashing and Character Hashing
# we need to define large elements for hash array
# eg: arr = [2,4,5,1,12,2,1,5]
# we create hash array of size 13- which is not needed, we only need to store for value
# 1,2,4,5,12  - other values are wasting the space

# So,
#-  Space optimized way
# we use map,unordered map in C++

# In map,
# Evreything is stored in sorted ordera{ascneding}
# for storing and fetching,time complexity is log(N) {N- Number of elements in MAP}
# - In all case,average,best and worst

# In unordered map
# Evreything is stored in unordered manner{ not sorted like unordered map}
# # for storing and fetching,time complexity is O(1) - In average,best case
# Worst case: O(N) {N- Number of elements in Unordered MAP}

# We cannot implement map in python but can implement unordered map using dictionary in python

# we use hash map in java

# eg: 
# arr = [1,2,3,1,3,2]
# map is a datastructure 
# map has key and value 
# key - Number/Element {1,2,3}
# value - Frequency {2,2,2}

# we are using dictionary to perform this idea
arr = [1,2,3,1,3,2]
# arr ="faxbcdbcf"
hash_dict ={x:0 for x in arr} 
print(hash_dict) # {'f': 0, 'a': 0, 'x': 0, 'b': 0, 'c': 0, 'd': 0}

#precompute
for i in range(len(arr)):
    hash_dict[arr[i]]+=1
print(hash_dict) # {'f': 2, 'a': 1, 'x': 1, 'b': 2, 'c': 2, 'd': 1}

# fetch
# print(hash_dict['f']) # 2
print(hash_dict[3])




# Time complexity:
# hash_dict - definition  O(N) and insertion average case: O(1) ,worst case: O(N) ,O(N*1)- O(N) / O(N*N)=O(N^2)
# frequency update in dict - loop runs for N times O(N), updation - average case: O(1),worst case: O(N),O(N*1) /  O(N*N)=O(N^2)
# fetch - average case:  O(1), worst case: O(N), O(1) / O(N)

# O(N) - happens in rare case becuase of collisions

# Final Time Complexity:(Average Case) O(N)+O(N)+O(1)= O(2N+1) ~= O(2N) ~= O(N)
# Final Time Complexity:(Worst Case) O(N^2)+O(N^2)+O(N)= O(2N^2+N) ~= O(2N^2) ~= O(N^2)

# Space Complexity : O(U) {U - No of unique values in given array}


# What is Collision and How hashing workS?
#- Division method
#- Folding method
#- Mid-Square method

# Division method:
# what if hashing array should not exceed size of 10 ?
# we use this method

# Eg: xin = [2, 5, 16, 28, 139]
# for the above array, we need to create hash array of size 140
# but we only use size as 10 as given.
# consider my hash array size is 10
# 2%10 =2
# 5%10 =5
# 16%10 =6
# 28%10 =8
# 139%10 =9

# Hashing & Prestoring
# 0-
# 1
# 2 - 2
# 3 
# 4 
# 5 -5
# 6- 16
# 7
# 8 - 28
# 9 - 139

# hash[xin[i]%10]+=1

# # fetching
# hash[number%10]


# What if two or more array elements give the same remainder for modulo 10?
"""
In this case, we apply the linear chaining method. This method is implemented using Linked List which will be discussed later in another article. Here, we just need to understand the logic. While storing the elements we will maintain a chain(i.e. inserting the element itself to the corresponding index instead of just keeping the count) for each index(i.e. the remainder we get). And in that chains, we will store the elements in a sorted fashion.
"""

# Let’s understand it considering the following example:

# Given array: [2, 5, 16, 28, 139, 38, 48, 28, 18]

# In this array 28, 38, 48, and 18 are giving the same value for modulo 10. So, we will apply linear chaining. The hash array will look like the following:

# 0
# 1
# 2->2
# 3
# 4
# 5->5
# 6-> 16
# 7
# 8 -> 18 -> 28 -> 28 -> 38 -> 48
# 9-> 139

# Now to get the frequency of a number, we will first go to (number % 10) indexed chain and count the frequency of that number.

# Note: We can choose to take modulo of any number as per our need. Here for example we have taken the number 10.

# # Collision
# Now, if we are applying linear chaining and division rule and we find that all elements of an array get stored in a single index, then we will call it a case of collision.

# Example:

# Given array: [8, 18, 28, 38, 48, 58, 68, ….., 1008]

# If we apply the methods and take modulo 10 for every number, the hash array will look like the following:

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8->8->18-> 28 -> 38 -> 1008
# 9

# Now, while fetching we have to traverse N times(N = size of the given array) to find the frequency of an element. This is when the worst case happens and the time complexity becomes O(N). But this happens very very rarely.

# Whatever method the map is using, if all the elements go to the same hash index, we will call it a case of collision.

# Note: In the map data structure, the data type of key can be anything like int, double, pair<int, int>, etc. But for unordered_map the data type is limited to integer, double, string, etc. We cannot have an unordered_map whose key is pair<int, int>.