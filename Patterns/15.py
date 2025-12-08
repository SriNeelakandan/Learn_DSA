def x(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65+j),end="")
        print(end="\n")
        
n=int(input())
x(n)
