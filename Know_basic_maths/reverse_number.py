# Bruteforce

n=input("Enter a number:")
print(int(n[::-1]))

# Time Complexity: O(log10N) — we process each digit to convert to string and reverse
# Space Complexity: O(log10N) — storing the string representation of the number
# -------------------------------------------------------------------------------------------------
# # Optimal approach
n=int(input("Enter a number: "))
res=0
while n>0:
    r=n%10
    res =r+ (10*res)
    n=n//10
print(res)

# # Time Complexity:
# # O(log10(number)+1) - loop runs for no of digits of a given number

# # Space Complexity:
# # O(1) - constant variables are used