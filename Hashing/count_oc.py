# Input: arr[] = {10,5,10,15,10,5};
# Output: 
# 10  3
# 5   2
# 15  1


# Bruteforce

# def display(d):
#     for x,y in d.items():
#         print(f"{x} - {y}",end="\n")
    

# def find_oc(x):
#     q_v=list(set(x))
#     count={x:0 for x in q_v}
#     for i in range(0,len(q_v)):
#         for j in range(0,len(x)):
#             if q_v[i] == x[j]:
#                 count[q_v[i]]+=1
#     return count

# xin = [10,5,10,15,10,5]
# print(display(find_oc(xin)))

# Time Complexity: O(N*N) {N- No of elements in Input array}
# Space Complexity: O(U) {U- No of unique elements}

# Using Unordered Map by dictionary
hash_dict={}

# Precompute
def precompute(xin):
    global hash_dict
    hash_dict={x:0 for x in xin}
    for i in range(0,len(xin)):
        hash_dict[xin[i]]+=1
    return hash_dict
# # Fetch
# def fetch(n):
#     return hash_dict[n]

xin = [10,5,10,15,10,5]
res=precompute(xin)
for x,y in res.items():
    print(f"{x}   -  {y}")


# Time Complexity: O(N) - Average case, O(N*N) - worst case
# Space Complexity: O(U) - Unique elements in given array