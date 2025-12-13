# Bubble sort

# Push the maximum to the last 
# By adjacent swapping


def bubble_sort(x,n):
    for i in range(n):
        didwap= False
        for j in range(n-i-1):
            if x[j]>x[j+1]:
                #swap(x[i],x[i+1])
                didwap = True
                x[j],x[j+1]=x[j+1],x[j]
        if didwap == False:
            print(f"breaked at {i}- {j}")
            break
        print(x)

    return x
x=list(map(int,input().split()))
n=len(x) # 6
print(bubble_sort(x,n))

# Time Complexity: O(N^2)
# Space Complexity: O(1)

# # When given array is already sorted,
# use didwap variable to make that best time complexity as O(N)
