from graph import Graph

from collections import deque


def dfs(G,v):
    """Depth First search using  for a vertex in a graph

    Args:
        G (_type_): Graph
        v (_type_): vertex for which we wanna do the DFS

    Returns:
        a dictionary showing path between all the vertices 
        connected to this vertex somehow
    """

    tree = {}  #stores vertex and its parent

    edgetovisit = [(None,v)]  #stack that stores the edges we want to visit, starts from and edge to "v"


    while edgetovisit:  #until the stack  is empty

        a,b = edgetovisit.pop() #first edge

        if b not in tree: 

            tree[b] = a  #adding b to our tree 

            for c in G.neighbours(b):

                edgetovisit.append((b,c))

    return tree



def connected(G,u,v):

    """ Returns if the two vertices in the graph are connected or not
    """

    return v in dfs(G,u)

def path(G,u,v):

    """ Return path between u and v """

    tree = dfs(G,v)
    
    if u in tree:
        path = []
        while u is not None:
            path.append(u)
            u = tree[u]
        return path


def bfs(G,v):
    """ First search using Queue for a vertex in a graph

    Args:
        G (_type_): Graph
        v (_type_): vertex for which we wanna do the BFS

    Returns:
        a dictionary showing path between all the vertices 
        connected to this vertex somehow
    """

    tree = {}  #stores vertex and its parent

    edgetovisit = deque()
    edgetovisit.append((None,v)) #queue that stores the edges we want to visit, starts from and edge to "v"


    while edgetovisit:  #until the queue is empty

        a,b = edgetovisit.popleft() #first edge

        if b not in tree: 

            tree[b] = a  #adding b to our tree 

            for c in G.neighbours(b):

                edgetovisit.append((b,c))

    return tree

if __name__ == "__main__":

    G = Graph([],'ab bc cd ad bd de ef gh'.split())
    # print(list(G.neighbours("c")))
    print(dfs(G,"f"))

    assert(connected(G,'a','f'))
    assert(not connected(G,'f','g'))

    print(path(G,"b","f"))

    print(bfs(G,"a"))