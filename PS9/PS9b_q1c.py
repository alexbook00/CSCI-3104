def PellNum(n):
    PellArray=[]
    for i in range(n+1):
        if i==0 or i==1:
            PellArray.append(1)
        else:
            PellArray.append(2*PellArray[i-1]+PellArray[i-2])
    return PellArray[-1]

if __name__ == '__main__':
    print(PellNum(5))
