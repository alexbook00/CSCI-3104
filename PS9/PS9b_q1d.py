def PellNum(n):
    minus2=0
    minus1=0
    current=0
    for i in range(n+1):
        if i==0 or i==1:
            minus2=1
            minus1=1
            current=1
        else:
            current=2*minus1+minus2
            minus2=minus1
            minus1=current
    return current

if __name__ == '__main__':
    print(PellNum(5))
