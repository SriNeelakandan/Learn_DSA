# 1
# 01
# 101
# 0101
# 10101

def fn11(n):
    for i in range(n):
        for j in range(i+1):
            if (i+j) %2 ==0:
                print(1,end=" ")
            else:
                print(0,end=" ")
        print(end="\n")

n=int(input())
fn11(n)