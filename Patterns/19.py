def g(n):
    
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        c=65
        for k in range((2*i)+1):
            print(chr(c),end=" ")
            if k < ((2*i)+1)//2:
                c+=1
            else:
                c-=1            
        for l in range(n-i-1):
            print(" ",end=" ")
        print(end="\n")

n=int(input())
g(n)