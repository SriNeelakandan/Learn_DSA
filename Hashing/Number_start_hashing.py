# Optimized Approach using Hashing

# Number Hashing
# xin = [1,4,5,1,3,4,5,2,1,2]
# We need to create 
#  dictionary {0: 0, 1: 3, 2: 2, 3: 1, 4: 2} for implementing Hashing

xin = [1,4,5,1,3,4,5,2,1,2]
hash_dict ={i:xin.count(i) for i in range(max(xin))}
q_v =int(input("Enter the Query Number: "))
print(hash_dict[q_v])