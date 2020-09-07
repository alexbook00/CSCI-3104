import numpy as np

def nsquared_flips(arr):
    count=0
    for i in range(len(arr)-1):
        for j in range (i+1,len(arr)):
            if arr[i] > arr[j]:
                count+=1
    return count

def mergeSort_flips(A,p,r):
    count=0
    if p < r:
        q=(p+r)//2
        count+=mergeSort_flips(A,p,q)
        count+=mergeSort_flips(A,q+1,r)
        count+=merge(A,p,q,r)
    return count

def merge(A,p,q,r):
    count=0
    i=0
    j=0
    k=p
    low=[]
    high=[]
    for x in range(p,q+1):
        low.append(A[x])
    for x in range(q+1,r+1):
        high.append(A[x])
    while i < (q-p+1) and j < (r-q):
        if low[i] <= high[j]:
            A[k]=low[i]
            i+=1
        else:
            A[k] = high[j]
            count+=(q-p+1-i) # i-th element and all following elements in low are flips
            j+=1
        k+=1
    while i < (q-p+1):
        A[k]=low[i]
        i+=1
        k+=1
    while j < (r-q):
        A[k]=high[j]
        j+=1
        k+=1
    return count

def allFlips(n):
    A=np.random.randint(n, size=n)
    return nsquared_flips(A),mergeSort_flips(A,0,len(A)-1)

if __name__ == '__main__':
    nsquared,nlogn=allFlips(2**12)
    print(nsquared)
    print(nlogn)
