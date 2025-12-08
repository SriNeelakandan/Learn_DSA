#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def b(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range((2*n)-((2*i)+1)):
            print("*",end="")
        for m in range(i):
            print(" ",end="")
        print(end="\n")

def t(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range((2*i) +1):
            print("*",end="")
        for l in range(n-i-1):
            print(" ",end="")
        print(end="\n")
        
n=int(input())
t(n)
b(n)