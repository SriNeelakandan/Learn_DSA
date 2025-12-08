# Rotate an array right by D places

# Bruteforce

# Input: [1,2,3,4,5,6] d=2
# Output: [5,6,1,2,3,4]

# def rotate(arr,n,d):
#     d=d%n
#     new_arr=[]
#     # pick those element
#     for i in range(n-d,n):
#         new_arr.append(arr[i])
    
#     #Shifting
#     for i in range(n-d-1,-1,-1):
#         arr[i+d]=arr[i]
    
#     # Place those picked elemnts to an array
#     for i in range(0,len(new_arr)):
#         arr[i]=new_arr[i]
    

# x=[1,2,3,4,5,6] 
# d=2
# rotate(x,len(x),d)
# print(x)

# Time Complexity: O(d) + O(n-d) + O(d)= O(n+d)
# Space Complexity: O(d)


# Optimal

# Input: [1,2,3,4,5,6] d=2
# Output: [5,6,1,2,3,4]

def reverse(arr,start,end):
    end=end-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

def rotate(arr,n,d):
    reverse(arr,n-d,n)
    reverse(arr,0,n-d)
    reverse(arr,0,n)

x=[1,2,3,4,5,6]
rotate(x,len(x),2)
print(x)

# Time Complexity:
# O(D) + O(N-D) + O(N) = O(2N)

# Space Complexity: O(1)