def t(n):
    for i in range(n):
        #stars
        for j in range(n-i):
            print("*",end=" ")
        for k in range(2*i):
            print("-",end=" ")
        for l in range(n-i):
            print("*",end=" ")
        print(end="\n")
    return b(n)

def b(n):
    for i in range(n-1,-1,-1):
        #stars
        for j in range(n-i):
            print("*",end=" ")
        for k in range(2*i):
            print("-",end=" ")
        for l in range(n-i):
            print("*",end=" ")
        print(end="\n")

n=int(input())
t(n//2)
# b(n)