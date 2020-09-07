def valleys(arr):
    quarter=(len(arr))//4
    ret=[]
    ret.append(findValleys(arr,0,quarter-1))
    ret.append(findValleys(arr,3*quarter,len(arr)-1))
    if len(ret)>0:
        return min(ret)
    else:
        return # no valley

def findValleys(arr,p,r):
    if p<=r:
        mid=p+(r-p)//2
        if arr[mid]<arr[mid-1] and arr[mid]<arr[mid+1]:
            return arr[mid] # valley found
        elif arr[mid]>arr[mid-1]:
            return findValleys(arr,p,mid)
        else:
            return findValleys(arr,mid,r)
    else:
        return

if __name__=='__main__':
    arr=[10,7,6,2,11,15,20,19,18,17,15,8,6,5,4,3,5,8,9,11]
    print(valleys(arr))
