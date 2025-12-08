# *****
# ****
# ***
# **
# *

# n= int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print(end="\n")


n =int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print(end="\n")