def print_name(n):
    if n==0:
        return
    print("Sri Neelakandan",end=" ")
    print_name(n-1)
print_name(1)

# Time Complexity: O(N), we print our name exactly N times.
# Space Complexity: O(N), stack space used for recursive calls.