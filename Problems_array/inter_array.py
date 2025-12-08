# Intersection

# x= [2,4,5,7,8,8,9]
# y= [1,3,4,5,7,7,9]
# Output: [4,5,7,9]

# Bruteforce:
# def inter(x,y):
#     res=[]
#     vis=[0]*len(y)
#     for i in range(0,len(x)):
#         for j in range(0,len(y)):
#             if x[i]==y[j] and vis[j]==0:
#                 res.append(x[i])
#                 vis[j]+=1
#                 break
#     print(res)        
# x= [2,4,5,7,8,8,9]
# y= [1,3,4,5,7,7,9]
# inter(x,y)

# Time Complexity: O(N1+N2)
# Space Complexity: O(N2)

# Optimal
def inter(x,y):
    res=[]
    i=0
    j=0
    while i<len(x) and j <len(x):
        if x[i]==y[j]:
            if x[i] not in res:
                res.append(x[i])
            i+=1
            j+=1
        else :
            if x[i]<y[j]:
                i+=1
            else:
                j+=1
    print(res)
        
x= [2,4,5,7,8,8,9]
y= [1,3,4,5,7,7,9]
inter(x,y)

# Time Complexity: O(N1+N2)
# Space Complexity: O(1)