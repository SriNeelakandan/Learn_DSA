# Function to check if a number is an Armstrong number
def isArmstrong(num):
    k = len(str(num))
    sum = 0
    n = num
    while n > 0:
        ld = n % 10
        sum += ld ** k
        n = n // 10
    return sum == num

number = int(input())
if isArmstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
#Time Complexity: O(log10N + 1) where N is the input number. The time complexity is determined by the number of digits in the input integer N. In the worst case when N is a multiple of 10 the number of digits in N is log10 N + 1.

# In the while loop we divide N by 10 until it becomes 0 which takes log10N iterations.
# In each iteration of the while loop we perform constant time operations like modulus and division and pushing elements into the vector.
# Space Complexity: O(1) as only a constant amount of additional memory for the reversed number regardless of size of the input number.