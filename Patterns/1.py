def p(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print("\n")

t=int(input())

for i in range(t):
    n=int(input())
    p(n)

