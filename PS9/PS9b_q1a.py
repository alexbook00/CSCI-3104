def PellNum(n):
    if n==0 or n==1:
        return 1
    else:
        return 2*PellNum(n-1)+PellNum(n-2)

if __name__ == '__main__':
    print(PellNum(5))
