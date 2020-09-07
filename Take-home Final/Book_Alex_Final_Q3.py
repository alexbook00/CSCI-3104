import numpy as np
import math

def epic(arr,L,R):
    # handles case of array of size zero
    if len(arr)==0:
        return 0
    # if the optimal sum has already been found, return it to prevent unneeded recursive calls
    if chooseArray[L][R] != math.inf:
        return chooseArray[L][R]
    # if the optimal sum must be found
    else:
        #if the cards are next to each other, Player 1 chooses the minimum of the two cards
        if L==R-1:
            chooseArray[L][R] = min(arr[L],arr[R])
            return min(arr[L],arr[R])
        # if P1 chooses left
        ifLeftL=L+1
        ifLeftR=R
        if arr[L+1]<=arr[R]: # if P2 chooses next left
            ifLeftL=L+2
        elif arr[R]<arr[L+1]: # if P2 chooses right
            ifLeftR=R-1
        # if P1 chooses right
        ifRightL=L
        ifRightR=R-1
        if arr[R-1]<arr[L]: # if P2 chooses next right
            ifRightR=R-2
        elif arr[L]<=arr[R-1]: # if P2 chooses left
            ifRightL=L+1
        chooseArray[L][R]=min(arr[L]+epic(arr,ifLeftL,ifLeftR),
                            arr[R]+epic(arr,ifRightL,ifRightR))
        return min(arr[L]+epic(arr,ifLeftL,ifLeftR),
                arr[R]+epic(arr,ifRightL,ifRightR))

size=100
chooseArray=[[math.inf for i in range(size)]for j in range(size)]

if __name__=="__main__":
    A=np.random.randint(1,10,size)
    print(A)
    L=0
    R=len(A)-1
    x=epic(A,L,R)
    print("P1 Score:",x)
    print("P2 Score:",sum(A)-x)
