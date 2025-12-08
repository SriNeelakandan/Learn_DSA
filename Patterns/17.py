def x(n):
    c=69
    for i in range(0,n):
        for j in range(c-i,c+1):
            print(chr(j),end=" ")
        print(end="\n")
        
n=int(input())
x(n)
