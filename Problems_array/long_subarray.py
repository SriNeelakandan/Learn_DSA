# Longest subarray with sum k

# Bruteforce:
# - Generate all sub arrays
# - Check the sum of sub array and whoever is the longest length
# - return the length

x=[1,1,1,1,2,3,1]
i=0
max_len=0
n=4
while i <len(x):
    j=i
    sum=0
    while j<len(x):
        sum+=x[j]
        # print(end="\n")
        j+=1
        if sum==n and (j-i)>max_len:
            max_len=(j-i)
    i+=1
print(max_len)