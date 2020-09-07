PellArray=[1,1]

def PellNum(n):
    if len(PellArray)-1 >= n:
        return PellArray[n]
    a=2*PellNum(n-1)+PellNum(n-2)
    PellArray.append(a)
    return a

if __name__ == '__main__':
    print(PellNum(5))
