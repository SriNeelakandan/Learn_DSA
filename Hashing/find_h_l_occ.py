# Bruteforce


def find_oc(x):
    q_v=list(set(x))
    count={x:0 for x in q_v}
    for i in range(0,len(q_v)):
        for j in range(0,len(x)):
            if q_v[i] == x[j]:
                count[q_v[i]]+=1
    return count

def max_min(x):
    m=max(x.values())
    n=min(x.values())
    for a,b in x.items():
        if b==m:
            m=a
        if b==n:
            n=a
    return m,n
        
xin = [10,5,10,15,10,5]
d= find_oc(xin)
print(f" Highest Frequency Number: {max_min(d)[0]}  - Lowest Frequency Number: {max_min(d)[1]} ")

# Time Complexity: O(N*N) {N- No of elements in Input array}
# Space Complexity: O(U) {U- No of unique elements}

# Using Unordered Map by dictionary
# hash_dict={}


# def max_min(x):
#     m=max(x.values())
#     n=min(x.values())
#     for a,b in x.items():
#         if b==m:
#             m=a
#         if b==n:
#             n=a
#     return m,n
# # Precompute
# def precompute(xin):
#     global hash_dict
#     hash_dict={x:0 for x in xin}
#     for i in range(0,len(xin)):
#         hash_dict[xin[i]]+=1
#     return hash_dict
# # # Fetch
# # def fetch(n):
# #     return hash_dict[n]

# xin = [10,5,10,15,10,5]
# res=precompute(xin)
# print(f" Highest Frequency Number: {max_min(res)[0]}  - Lowest Frequency Number: {max_min(res)[1]} ")



# Time Complexity: O(N) - Average case, O(N*N) - worst case
# Space Complexity: O(N)

# print(max(res.values()))