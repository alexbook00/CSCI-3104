import numpy as np
import matplotlib.pyplot as plt

def h1(x):
    codeSum=0
    for i in range(len(x)):
        codeSum+=ord(x[i])-64 # ASCII value for A is 65
    return codeSum%5987

def h2(x):
    codeSum=0
    for i in range(len(x)):
        codeSum+=(ord(x[i])-64)*np.random.randint(0,5986)
    return codeSum%5987

if __name__=='__main__':

    # FIGURE FOR PART D

    maxArrayH2=[]
    for q in range(5000):
        file=open("dist.all.last.txt","r")
        names=[]
        i=q
        j=0
        while i>0 and j<88798:
            line=file.readline()
            name=line.split()
            boolean=np.random.randint(0,2)
            if boolean==1:
                #print(name[0])
                names.append(name[0])
                i-=1
            j+=1
        #hashLocationsH1=[0 for x in range(5987)]
        hashLocationsH2=[0 for y in range(5987)]
        for n in names:
            #indexH1=h1(n)
            indexH2=h2(n)
            #hashLocationsH1[indexH1]+=1
            hashLocationsH2[indexH2]+=1
        maxArrayH2.append(max(hashLocationsH2))

    plt.figure(figsize=(12,6))
    plt.plot(maxArrayH2)
    plt.title("Max chain sizes using h2")
    plt.xlabel("Number of names")
    plt.ylabel("Max chain size")
    plt.show()

    ##############################################

    # FIGURE FOR PART C

    # maxArrayH1=[]
    # for q in range(5000):
    #     file=open("dist.all.last.txt","r")
    #     names=[]
    #     i=q
    #     j=0
    #     while i>0 and j<88798:
    #         line=file.readline()
    #         name=line.split()
    #         boolean=np.random.randint(0,2)
    #         if boolean==1:
    #             #print(name[0])
    #             names.append(name[0])
    #             i-=1
    #         j+=1
    #     hashLocationsH1=[0 for x in range(5987)]
    #     #hashLocationsH2=[0 for y in range(5987)]
    #     for n in names:
    #         indexH1=h1(n)
    #         #indexH2=h2(n)
    #         hashLocationsH1[indexH1]+=1
    #         #hashLocationsH2[indexH2]+=1
    #     maxArrayH1.append(max(hashLocationsH1))
    #
    # plt.figure(figsize=(12,6))
    # plt.plot(maxArrayH1)
    # plt.title("Max chain sizes using h1")
    # plt.xlabel("Number of names")
    # plt.ylabel("Max chain size")
    # plt.show()

    ##############################################

    # FIGURES FOR PARTS A & B
    #
    # names=[]
    # file=open("dist.all.last.txt","r")
    #
    # i=44399
    # j=0
    # while i>0 and j<88798:
    #     line=file.readline()
    #     name=line.split()
    #     boolean=np.random.randint(0,2)
    #     if boolean==1:
    #         names.append(name[0])
    #         i-=1
    #     j+=1
    # hashLocationsH1=[0 for x in range(5987)]
    # hashLocationsH2=[0 for y in range(5987)]
    # for n in names:
    #     indexH1=h1(n)
    #     indexH2=h2(n)
    #     hashLocationsH1[indexH1]+=1
    #     hashLocationsH2[indexH2]+=1
    #
    # histArrayH1=[]
    # histArrayH2=[]
    #
    # for c in range(len(hashLocationsH1)):
    #     for d in range(hashLocationsH1[c]):
    #         histArrayH1.append(c)
    #
    # for e in range(len(hashLocationsH2)):
    #     for f in range(hashLocationsH2[e]):
    #         histArrayH2.append(e)
    #
    # plt.figure(figsize=(12,6))
    # plt.hist(histArrayH1,bins=5987)
    # plt.title("Using h1")
    # plt.xlabel("Bin")
    # plt.ylabel("Frequency")
    # plt.show()
    #
    # plt.figure(figsize=(12,6))
    # plt.hist(histArrayH2,bins=5987)
    # plt.title("Using h2")
    # plt.xlabel("Bin")
    # plt.ylabel("Frequency")
    # plt.show()
