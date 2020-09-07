def healthShake(p,c,C):
    #create empty 2D array full of zeros
    bestShakes = [[0 for i in range(C+1)] for j in range(len(p)+1)]
    #start for loops at 1 in order to skip the base case rows and columns
    for i in range(1,len(p)+1): #i is ingredient being considered
        protein=p[i-1] #keeps track of protein for ingredient being considered
        calories=c[i-1] #keeps track of calories for ingredient being considered
        for j in range(1,C+1): #j is capacity being considered
            if calories > j:
                #need to use max. protein from previous ingredient consideration
                bestShakes[i][j]=bestShakes[i-1][j]
            else:
                #need to take max. protein from either previous ingredient
                #consideration or the value that would come before the
                #current (one ingredient earlier and capacity minus current
                #ingredient's calories
                bestShakes[i][j]=max(bestShakes[i-1][j],
                protein+bestShakes[i-1][j-calories])
    return bestShakes[len(p)][C]

if __name__ == '__main__':
    p=[4,4,3,1]
    c=[7,2,6,3]
    C=12
    print(healthShake(p,c,C))
