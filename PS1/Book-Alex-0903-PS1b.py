import numpy as np

def flips(n):
    A=np.random.randint(n, size=n)
    count=0
    for i in range(n):
        for j in range (i+1,n):
            if A[i] > A[j]:
                count+=1
    return count
