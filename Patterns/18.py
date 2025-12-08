def f_min(x,y):
    if x<=y:
        return x
    else:
        return y

def x(n):
    for i in range(0,(2*n)-1):
        for j in range(0,(2*n)-1):
            top =i
            left =j
            bottom = ((2*n)-1)-1 -i
            right = ((2*n)-1)-1 -j
            val = 4- (f_min(f_min(top,bottom),f_min(left,right)))
            print(val,end=" ")
        print(end="\n")

n=int(input())
x(n)