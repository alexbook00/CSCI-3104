class graph:
    def __init__(self,G):
        self.graph=G
        self.numRows=len(G)
        self.numCols=len(G[0])
        self.visited=[[False for k in range(self.numCols)] for l in range(self.numRows)]
    def exists(self,i,j):
        return(
        (i>=0) and
        (j>=0) and
        (i<self.numRows) and
        (j<self.numCols)
        )
    def DFS(self,i,j,size):
        self.visited[i][j]=True
        if self.exists(i-1,j-1) and not self.visited[i-1][j-1] and self.graph[i-1][j-1]==0:
            size+=self.DFS((i-1),(j-1),size) #up and to the left
        if self.exists(i-1,j) and not self.visited[i-1][j] and self.graph[i-1][j]==0:
            size+=self.DFS((i-1),(j),size) #straight up
        if self.exists(i-1,j+1) and not self.visited[i-1][j+1] and self.graph[i-1][j+1]==0:
            size+=self.DFS((i-1),(j+1),size) #up and to the right
        if self.exists(i,j-1) and not self.visited[i][j-1] and self.graph[i][j-1]==0:
            size+=self.DFS((i),(j-1),size) #straight left
        if self.exists(i,j+1) and not self.visited[i][j+1] and self.graph[i][j+1]==0:
            size+=self.DFS((i),(j+1),size) #straight right
        if self.exists(i+1,j-1) and not self.visited[i+1][j-1] and self.graph[i+1][j-1]==0:
            size+=self.DFS((i+1),(j-1),size) #down and to the left
        if self.exists(i+1,j) and not self.visited[i+1][j] and self.graph[i+1][j]==0:
            size+=self.DFS((i+1),(j),size) #straight down
        if self.exists(i+1,j+1) and not self.visited[i+1][j+1] and self.graph[i+1][j+1]==0:
            size+=self.DFS((i+1),(j+1),size) #down and to the right
        return size

def pondSizes(g):
    ponds=[]
    for i in range(g.numRows):
        for j in range(g.numCols):
            if not g.visited[i][j] and g.graph[i][j]==0:
                ponds.append(g.DFS(i,j,1))
    return ponds

grph=[
    [0,2,1,0],
    [0,1,0,1],
    [1,1,0,1],
    [0,1,0,1]
    ]
#grph=[[0,2]]
#grph=[
#    [0,0,0,1,0,1,0],
#    [1,1,1,0,1,1,1],
#    [1,1,1,1,1,1,0],
#    [1,1,1,0,1,0,1]
#    ]

g = graph(grph)
print(pondSizes(g))
