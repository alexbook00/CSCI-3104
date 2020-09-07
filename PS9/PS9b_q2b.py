def whichAssignments(A):
    maxPoints=[]
    for i in range(len(A)):
        if i==0:
            #max points for only one assignment must be the value of the first assignment
            maxPoints.append(A[i])
        elif i==1:
            #max points between the first two assignments is simply the higher of the two
            maxPoints.append(max(A[i],A[i-1]))
        else:
            #max points otherwise is considered between adding the current value to
            #the value two before it versus simply copying the value of one before it
            maxPoints.append(max(maxPoints[i-2]+A[i],maxPoints[i-1]))
    #returns the value of the last element in the maxPoints array, as that
    #is the maximum value considering all homework assignments
    return maxPoints[-1]

if __name__ == '__main__':
    A=[2,7,9,3,1]
    print(whichAssignments(A))
