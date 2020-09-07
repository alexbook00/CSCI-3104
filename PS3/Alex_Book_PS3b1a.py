def stopCounter(k,pods=[]):
    lastStop=0
    finalList = []
    for i in range(0,len(pods)):
        if pods[i]-pods[lastStop] > k:
            finalList.append(pods[i-1])
            lastStop=i-1
    print(finalList)
