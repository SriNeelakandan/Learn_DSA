# Remove duplicates inplace from sorted array
# return no of unique elements,place those unique elements from the first of original array
# Input: x=[1,1,1,2,2,3,3,3]
# Output : x=[1,2,3,_,_,_,_,_] - return 3

# Bruteforce
# x=[1,6,4,5,6,7,6,7]
# y=list(set(x))
# print(y)
# for i in range(0,len(y)):
#     x[i]=y[i]
# print(x)

# Time Complexity:
# Convert to set - takes NlogN - times
# Modifying the list elements - N times
# So, it is O(NlogN) + O(N)

# Space Complexity: O(N) - If all are unique elements

# Better approach

# def rem_d(arr):
#     unique=[]

#     # unique elements
#     for i in arr:
#         if i not in unique:
#             unique.append(i)
#     print(unique)
#     for j in range(len(unique)):
#         arr[j]=unique[j]
    
#     return arr

# x=[1,1,2,2,2,3,6,7]
# print(rem_d(x))


# Time Complexity: O(N)+O(N)
# Space Complexity: O(N)

# Optimal Approach:

# x=[1,2,3,4,5]
def rm_d(x):
    first=0
    for j in range(1,len(x)):
        if x[j]!=x[first]:
            first+=1
            x[first]=x[j]
    return first+1

x=[1,1,2,2,2,3,3,3,4]
print(rm_d(x))
print(x)
# Time Complexity: O(N)

# Space Complexity: O(1)