from pprint import pprint
import random

def alignStrings(x,y,c_insert,c_delete,c_sub):
    S=[[0 for a in range(len(y)+1)] for b in range(len(x)+1)]
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if i==0:
                S[i][j]=j
            elif j==0:
                S[i][j]=i
            elif x[i-1]==y[j-1]:
                S[i][j]=S[i-1][j-1]
            else:
                S[i][j]=min(S[i-1][j-1]+c_sub,
                            S[i][j-1]+c_insert,
                            S[i-1][j]+c_delete)
    return S

def extractAlignment(S,x,y,c_insert,c_delete,c_sub):
    operations=[]
    i=len(x)
    j=len(y)
    while i>0 or j>0:
        if x[i-1]==y[j-1]:
            operations.append("no-op")
            i-=1
            j-=1
        else:
            sv=S[i-1][j-1]+c_sub
            iv=S[i][j-1]+c_insert
            dv=S[i-1][j]+c_delete
            if sv<iv and sv<dv:
                operations.append("sub")
                i-=1
                j-=1
            elif iv<sv and iv<dv:
                operations.append("insert")
                j-=1
            elif dv<sv and dv<iv:
                operations.append("delete")
                i-=1
            else:
                if sv==iv and sv==dv: # sub, insert, and delete tied
                    n=random.randint(1,3)
                    if n==1:
                        operations.append("sub")
                        i-=1
                        j-=1
                    elif n==2:
                        operations.append("insert")
                        j-=1
                    elif n==3:
                        operations.append("delete")
                        i-=1
                elif sv==iv: # sub and insert tied
                    n=random.randint(1,2)
                    if n==1:
                        operations.append("sub")
                        i-=1
                        j-=1
                    elif n==2:
                        operations.append("insert")
                        j-=1
                elif sv==dv: # sub and delete tied
                    n=random.randint(1,2)
                    if n==1:
                        operations.append("sub")
                        i-=1
                        j-=1
                    elif n==2:
                        operations.append("delete")
                        i-=1
                elif iv==dv: # insert and delete tied
                    n=random.randint(1,2)
                    if n==1:
                        operations.append("insert")
                        j-=1
                    elif n==2:
                        operations.append("delete")
                        i-=1
    operations.reverse()
    return operations

def commonSubstrings(x,L,a):
    ret=[]
    current=[]
    x_i=0
    for a_i in range(len(a)):
        if a[a_i]=="no-op":
            current.append(x[x_i])
            x_i+=1
        elif a[a_i]=="insert":
            if(len(current)>=L):
                ret.append(''.join(current))
            current=[]
        else:
            if(len(current)>=L):
                ret.append(''.join(current))
            current=[]
            x_i+=1
    if len(current)>=L:
        ret.append(''.join(current))
    return ret

if __name__ == "__main__":
    x="EXPONENTIAL"
    y="POLYNOMIAL"
    # x=open("Song1_Folsom_Prison.txt","r").read()
    # y=open("Song2_Crescent_City_Blues.txt","r").read()
    c_insert=2
    c_delete=1
    c_sub=2
    S=alignStrings(x,y,c_insert,c_delete,c_sub)
    E=extractAlignment(S,x,y,c_insert,c_delete,c_sub)
    C=commonSubstrings(x,2,E)
    pprint(S)
    print(E)
    print(C)
