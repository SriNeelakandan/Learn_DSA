
def max_min(d):
    s_d= sorted(d.items(),key= lambda item:item[1],reverse=True)
    return s_d


def give_occ(x):
    count={i:0 for i in x}
    for i in x:
        count[i]+=1
    return count

x=[10,5,10,15,10,5]
a = (give_occ(x))
print(a)
f= max_min(a)
print(f"Highest - {f[0][0]} , Lowest - {f[-1][0]}")

