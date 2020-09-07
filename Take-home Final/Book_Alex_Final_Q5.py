from pprint import pprint

# USE 3D ARRAY
# Priority right above in same k table
# 2nd priority diagonal in previous k table

# Runtime analysis:
# There are three nested for loops with dimensions, k, n, and t, respectively.
# The rest of the function runs in constant time.
# The operations in the nested loops run in constant time, so the entire function is O(n*t*k).

def SubarrayWithSum(S,t,k):
    sumArray=[[[ [False,[]] for z in range(t+1)] for y in range(len(S)+1)] for x in range(k+1)]
    for i in range(len(S)+1):
        sumArray[0][i][0][0]=True
    for i in range(1,k+1): # k value
        for j in range(1,len(S)+1): # index in given array
            for m in range(1,t+1): # counting up to given target sum
                # current item is too large to add to the sum subarray
                if S[j-1]>m:
                    sumArray[i][j][m]=sumArray[i][j-1][m]
                # current item doesn't need to be added because previous item did the trick
                elif sumArray[i][j-1][m][0]==True:
                    sumArray[i][j][m]=sumArray[i][j-1][m]
                # current item should be added if it would make a satisfying subarray
                elif sumArray[i-1][j-1][m-S[j-1]][0]==True:
                    sumArray[i][j][m][0]=True
                    sumArray[i][j][m][1]=list(sumArray[i-1][j-1][m-S[j-1]][1])
                    sumArray[i][j][m][1].append(S[j-1])
                # current item can't be added, so just copy the cell above in the same k table
                else:
                    sumArray[i][j][m]=sumArray[i][j-1][m]
    if sumArray[k][len(S)][t][0]==True:
        return sumArray[k][len(S)][t][1]
    else:
        return sumArray[k][len(S)][t][0]

if __name__=="__main__":
    S=[1,2,3,5,7]
    t=8
    k=3
    pprint(SubarrayWithSum(S,t,k))
