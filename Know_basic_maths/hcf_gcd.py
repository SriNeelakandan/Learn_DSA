# Brute force approach:
#- get minimum of two numbers
#- find the factor that divides two numbers and leaves a remainder 0
#- run from number 1 to min(two number)+1
#- The gcd value can be found even with few iterations or more iterations

a,b=map(int,input().split())
def gcd(a,b):
    res=0
    for i in range(1,min(a,b)+1):
        if a % i ==0 and b % i == 0:
            res =i
    return res
print(gcd(a,b))

# Time Complexity: O(min(a,b))
# Space Complexity: O(1)

#-------------------------------------------------------------------
# Better Approach
#- since we need to find greatest (highest common factor), 
#- we can run our loop to find the factor from highest to smallest, complexitites are same but finding the common factor can be obtained early compared to the above

def findgcd(a,b):
    res=0
    for i in range(min(a,b),0,-1):
        if a%i ==0 and b%i ==0:
            res =i
            return res


print(findgcd(12,18))
#Time Complexity: O(min(a,b))
#Space Complexity: O(1)
#----------------------------------------------------------------
# # Optimal Approach -recursion
def gcd(a,b):
    if b==0:
        return a
    elif a==0:
        return b
    else:
        return gcd(b,a%b)

# print(gcd(12,18))

# # Time Complexity : O(log(min(a,b)))
# # Space Complexity : O(log(min(a,b)))
#-----------------------------------------------
def gcd(x,y):
    while x>0 and y>0:
        if x>y:
            x=x%y
        else:
            y=y%x
    if x==0:
        return y
    return x

print(gcd(12,18))