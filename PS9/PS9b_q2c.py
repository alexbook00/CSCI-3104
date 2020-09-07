def whichAssignments_Oof1(A):
    #initialize all variables that will be written and read throughout
    #the algorithm
    minus2=0
    minus1=0
    current=0
    for i in range(len(A)):
        #all cases are the same as the version that fills the array, but this
        #time simply reads then reassigns variables for O(1) space complexity
        if i==0:
            minus2=A[i]
            minus1=A[i]
            current=A[i]
        elif i==1:
            current=max(minus1,A[i])
            minus1=current
        else:
            current=max(minus2+A[i],minus1)
            minus2=minus1
            minus1=current
    return current

if __name__ == '__main__':
    A=[2,7,9,3,1]
    print(whichAssignments_Oof1(A))
