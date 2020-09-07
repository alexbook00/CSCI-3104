"""
@author: Rhoenigman
         Shivendra
"""
import networkx as nx
import math

"""
The function to generate the input graph

:return: Returns the NetworkX Graph for Q2
"""
def Question2():
    # Create a directed graph
    G = nx.DiGraph()

    # The 'length' on each edge should be ignored and is only for drawing.
    # Adding an edge also adds the node
    G.add_edge('EC', 'A', length=40, weight=1.0)
    G.add_edge('EC', 'H', length=40, weight=1.0)
    G.add_edge('EC', 'J', length=60, weight=1.0)

    G.add_edge('H', 'G', length=40, weight=1.0)
    G.add_edge('H', 'K', length=40, weight=1.0)

    G.add_edge('G', 'L', length=40, weight=1.0)
    G.add_edge('G', 'F', length=40, weight=1.0)

    G.add_edge('F', 'E', length=40, weight=1.0)

    G.add_edge('E', 'HUMN', length=40, weight=1.0)

    G.add_edge('J', 'S', length=80, weight=1.0)
    G.add_edge('J', 'K', length=60, weight=1.0)

    G.add_edge('K', 'L', length=40, weight=1.0)
    G.add_edge('L', 'M', length=40, weight=1.0)
    G.add_edge('M', 'N', length=40, weight=1.0)
    G.add_edge('M', 'F', length=60, weight=1.0)

    G.add_edge('N', 'O', length=80, weight=1.0)
    G.add_edge('N', 'E', length=80, weight=1.0)

    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('A', 'S', length=60, weight=1.0)
    G.add_edge('A', 'B', length=40, weight=1.0)

    G.add_edge('B', 'R', length=40, weight=1.0)
    G.add_edge('B', 'C', length=40, weight=1.0)

    G.add_edge('S', 'R', length=60, weight=1.0)
    G.add_edge('R', 'Q', length=40, weight=1.0)

    G.add_edge('Q', 'C', length=40, weight=1.0)
    G.add_edge('Q', 'P', length=60, weight=1.0)

    G.add_edge('C', 'D', length=40, weight=1.0)
    G.add_edge('D', 'HUMN', length=40, weight=1.0)
    G.add_edge('P', 'D', length=40, weight=1.0)
    G.add_edge('P', 'O', length=60, weight=1.0)
    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('T', 'Q', length=40, weight=1.0)
    G.add_edge('T', 'P', length=40, weight=1.0)
    G.add_edge('T', 'O', length=40, weight=1.0)
    G.add_edge('T', 'N', length=40, weight=1.0)
    G.add_edge('T', 'M', length=40, weight=1.0)

    G.add_edge('R', 'T', length=40, weight=1.0)
    G.add_edge('S', 'T', length=40, weight=1.0)
    G.add_edge('J', 'T', length=40, weight=1.0)
    G.add_edge('K', 'T', length=40, weight=1.0)
    G.add_edge('L', 'T', length=40, weight=1.0)

    return G


"""
A utility function to help visualize the generated graph

:param G: NetworkX Graph
:return: None (instead saves the input graph in .png format)
"""
def draw_graph(G):
    import matplotlib.pyplot as plt
    import pylab
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    node_labels = {node: node for node in G.nodes()}

    pos = nx.spectral_layout(G)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_size=500, edge_cmap=plt.cm.Reds)
    plt.savefig('Finals_Q2_Graph.png')
    pylab.title("Input Graph")
    pylab.show()

def kStops(G,curr,end,k):
    ret=[]
    minSoFar=math.inf
    if curr==end and k==0: # reached the end node in k stops
        return [end],0
    if k < 0 or len(list(G.neighbors(curr)))==0: # you've went too far to achieve only k stops OR current node has no neighbors
        return [curr],minSoFar
    else: # explore next node
        for next in G.neighbors(curr):
            curr_next_edgeWeight=G.edges[curr,next]['weight'] # weight of edge between current and next
            if curr_next_edgeWeight+kStops(G,next,end,k-1)[1]<minSoFar: # if that path is viable and shorter than the previous viable paths
                minSoFar=curr_next_edgeWeight+kStops(G,next,end,k-1)[1] # weight of shortest viable path if it exists
                ret=kStops(G,next,end,k-1)[0] # rest of vertices of shortest viable path if it exists
        ret.append(curr) # append current nodes
    return ret,minSoFar

def main():
    ################## READ CAREFULLY ##############################

    # Note that you cannot use any networkx functionality
    # which makes the solution trivial

    # The 'length' on each edge (while generating the graph)
    # should be ignored and is only for drawing.
    # You should consider the 'weight' for finding the smallest path.
    # The above example has weights 1 but the weight can be anything.
    # Later on we may post some more graphs for testing.
    G = Question2()
    draw_graph(G)
    ret=kStops(G,'EC','HUMN',6)
    if ret[1]==math.inf:
        print('There is no k-stop path.')
    else:
        ret[0].reverse()
        print('Shortest path:',ret[0])
        print('Weight of shortest path:',ret[1])

    # Call your function here that takes in the Graph "G"
    # and returns the shortest path
    # (note that it is not the length but the entire path)





if __name__ == "__main__":
    # The driver function
    main()
