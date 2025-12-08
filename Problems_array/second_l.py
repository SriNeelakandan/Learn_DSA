# Second largest

def second_largest(x):
    flar=x[0]
    slar = -1 # assuming elements are non negative
    for i in range(1,len(x)):
        if x[i]>flar:
            slar=flar
            flar=x[i]
        elif x[i]<flar and x[i]>slar:
            slar=x[i]
    return slar

x=[12,12,8,4,1,0,8,9,10,11,11,11]
print(f"Second Largest in {x} is {second_largest(x)}")

# Time Complexity: O(N)
# Space Complexity: O(1)
