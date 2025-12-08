# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def t(n):
    for i in range(n//2 +1):
        for j in range(i+1):
            print("*",end=" ")
        print(end="\n")
        
def b(n):
    for i in range(n//2):
        for j in range(n//2 -i):
            print("*",end=" ")
        print(end="\n")

n=int(input())
t(n)
b(n)