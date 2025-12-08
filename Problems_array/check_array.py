# Check given array is sorted or not - ascending order

# A normal one
# x= [4,6,2,1,2,3,4]
# x=[1,2,3,4,5,6,1,5]
# x=[1,1,1,2,2,3,4,6,10]
# # sorted_ = False
# i=1
# while(i<len(x)):
#     if x[i]>= x[i-1]:
#         sorted_ = True
#         i+=1
#     else:
#         sorted_ = False
#         break


# if sorted_:
#     print(f"Given array {x} is sorted")
# else:
#     print(f"Given array {x} is not sorted")

# Time Complexity: O(N)
# Space Complexity: O(1)

# Using a function:
def check_array(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

x= [4,6,2,1,2,3,4]
print(check_array(x))
x=[1,2,3,4,5,6,1,5]
print(check_array(x))
x=[1,1,1,2,2,3,4,6,10]
print(check_array(x))
# Time Complexity: O(N)
# Space Complexity: O(1)
