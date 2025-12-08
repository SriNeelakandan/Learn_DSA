def print_number(c,n):
    if c>n:
        return
    print(c,end=" ")
    print_number(c+1,n)


    

print_number(1,4)

# Time Complexity: O(N), we print every number from 1 to N using recursion
# Space Complexity: O(N), stack space used for recursive calls.