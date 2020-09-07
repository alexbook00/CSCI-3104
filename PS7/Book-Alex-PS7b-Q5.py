import numpy as np
from random import shuffle

def partition(A,p):
    # partitions array A into 3 sections:
    # left = elements less than p, in order that they appear in A
    # equal = singleton array of element in A that is equal to p
    # right = elements greater than p, in order that they appear in A
    left=[]
    equal=[]
    right=[]

    for i in A:
        if i<p:
            left.append(i)
        if i>p:
            right.append(i)
        if i==p:
            equal.append(i)
    #print(left,equal,right)
    return left,equal,right

def bottlesCapsSort(bottles,caps):
    if len(bottles)<=1 and len(caps)<=1:
        return bottles,caps # if the passed arrays are only 1 item, they are already sorted
    sortedBottles = []
    sortedCaps = []
    x=caps[-1] # pivot to sort bottles is last element in caps
    leftB,equalB,rightB = partition(bottles,x)
    leftC,equalC,rightC = partition(caps,equalB[0]) # uses sorted term in bottles to sort caps
    solvedLeftB,solvedLeftC = bottlesCapsSort(leftB,leftC)
    solvedRightB,solvedRightC = bottlesCapsSort(rightB,rightC)
    # append items from left first so it is in ascending order
    sortedBottles.extend(solvedLeftB)
    sortedBottles.extend(equalB)
    sortedBottles.extend(solvedRightB)

    sortedCaps.extend(solvedLeftC)
    sortedCaps.extend(equalC)
    sortedCaps.extend(solvedRightC)

    return sortedBottles,sortedCaps

if __name__=='__main__':
    bottles=[]
    caps=[]
    for i in range (0,100):
        x=np.random.randint(0,100)
        bottles.append(x)
        caps.append(x)
    shuffle(bottles)
    shuffle(caps)
    print(bottles)
    print(caps)
    sortedBottles,sortedCaps=bottlesCapsSort(bottles,caps)
    print(sortedBottles)
    print(sortedCaps)
