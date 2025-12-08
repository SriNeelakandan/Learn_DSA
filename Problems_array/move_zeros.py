# move zeros to end
# Input: [1,0,4,7,0,2,0,0,3,0]
# Output: [1,4,7,2,3,0,0,0,0,0]

# def move(arr,n):
#     new_arr=[]
#     for i in range(0,n):
#         if arr[i] !=0:
#             new_arr.append(i)
    
#     for i in range(0,len(new_arr)):
#         arr[i]=new_arr[i]
    
#     for i in range(len(new_arr),n):
#         arr[i]=0


# x=[1,0,4,7,0,0,0,2,0,0,3,0]
# move(x,len(x))
# print(x)

# Time Complexity:
# O(N) + O(Nz) + O(N-Nz) = O(2N)

# Space Complexity:
# O(Nz) ~= O(N)


def move(x,n):
    j=-1
    # pick first zero
    for i in range(n):
        if x[i]==0:
            j=i
            break
    
    # traverse the array
    for i in range(j+1,n,1):
        if x[i]!=0:
            x[j],x[i]=x[i],x[j]
            j+=1
    return x 


x=[1,0,4,7,0,2,0,0,3,0]
# x=[1,2,3,4]
print(x)
print(move(x,len(x)))

# Time Complexity:
# O(Zp) + O(N-Zp)= O(N)
# Space Complexity: O(1)