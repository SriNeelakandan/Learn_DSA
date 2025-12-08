# Input : [3,1,2,1,4,3]
# Query value = [3,5,4,1,2]
# output = [2,0,1,2,1]
# Number 

# Bruteforce Approach
def check(q,x):
    cnt =[0] * len(q)
    for j in range(0,len(q)):
        for i in range(0,len(x)):
            if q[j] == x[i]:  
                    cnt[j]+=1
    return cnt

xin = [3,1,2,1,4,3]
q_v = [3,5,4,1,2]
print(f"Input Number: {xin}")
print(f"Query Number : {q_v}")
print(f"No of Occurrences: {check(q_v,xin)}")

# Time Complexity: 
# The outer loop runs for say M times (M - length of Query array)
# The inner loop runs for say N times (N - length of Input array)
# So total operations inside that loops are run for M*N times
# Hence, Time Complexity is O(M*N)

# Space Complexity: 
# The resulted occurence array of same length as Query array
# Space Complexity: O(M)

# Now, if the length of the query becomes large like 10^5 and the array size also becomes large like 10^5, the time complexity will be O(10^10).

# We know from our previous knowledge that 108 operations take 1 second to get executed. So, 1010 operations will take around 100 seconds(1010/108). We cannot say a code is good if it takes 100 seconds to get executed.