# xin ="abcdabefc"
# q_v =[a,c,z]
# output= [2,2,0]


# # Uppercase Input
# xin ="NEELS"
# print(xin)
# hash_dict = {x: xin.count(chr(x)) for x in range(ord(min(xin)),ord(max(xin))+1)}
# print(hash_dict)
# q_v=input("Enter a character: ")
# print(hash_dict[ord(q_v)])


# # Lowercase Input
# xin ="srineelakandan"
# print(xin)
# hash_dict = {x: xin.count(chr(x)) for x in range(ord(min(xin)),ord(max(xin))+1)}
# print(hash_dict)
# q_v=input("Enter a character: ")
# print(hash_dict[ord(q_v)])

xin ="sriNEELSneelakandansriram"
print(xin)
hash_dict = {x: xin.count(chr(x)) for x in range(ord(min(xin)),ord(max(xin))+1)}
print(hash_dict)
q_v=input("Enter a character: ")
print(hash_dict[ord(q_v)])