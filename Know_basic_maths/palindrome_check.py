# Bruteforce
n=input("Enter a number:")
rev= int(n[::-1])
n=int(n)
print(rev)
print("Palindrome" if (n==rev) else "Not a Palindrome")

# Time Complexity: O(n) - slicing happens for entire digits of a number
# Space Complexity: O(n) - reversed value is stored

# Optimal Approach
n=int(input("Enter a number: "))
def check_no(n):
    temp =n
    rev=0 
    while n>0:
        r=n%10
        rev=(rev*10 )+ r
        n=n//10
    if rev == temp:
        return True
    return False

print(check_no(n))

# Time Complexity: - O(log10(n)+1) - no of digits
# Space complexity: - O(1) - various constants are used