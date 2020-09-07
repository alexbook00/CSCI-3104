def h_value(A,p,r,h):
    q=(p+r)//2
    if A[q]>=q+1 and q+1>h:
        h=q+1
    if p < r:
        h=h_value(A,p,q-1,h)
        h=h_value(A,q+1,r,h)
    return h

if __name__ == '__main__':
    h=0
    A=[6,5,3,1,0]
    h=h_value(A,0,len(A)-1,0)
    print(h)
