# Second smallest

def second_smallest(x):
    fsmall = x[0]
    ssmall = max(x)+1
    for i in range(1,len(x)):
        if x[i]<fsmall:
            ssmall = fsmall
            fsmall = x[i]
        elif x[i] > fsmall and x[i]< ssmall:
            ssmall=x[i]
    return ssmall

x=[12,8,4,2,2,2,2,3,2,0,8,9]
print(f"Second smallest in {x} is : {second_smallest(x)}")

# Time Complexity: O(N)
# Space Complexity: O(1)