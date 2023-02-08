from graph import Graph
from graphSearch import dfs
import queue

def isConnected(G):

    """ Checks if graph G is connected or not
    """
    v = G.anyvertex()

    return len(dfs(G,v)) == G.n #if the num of keys of dfs tree of G is equal to 
                                #total num of vertices of G we are good to go



def isEulerian(G):

    """ 
    Check if there is a Euler Tour in graph G 
    """

    return isConnected(G) and all(G.deg(v)%2 == 0 for v in G.V)


def eulertour(G):
    """
    Returns Euler tour present in a graph
    """

    pass


def eulerTour_m2(G):
    
    if isEulerian(G):
        v = next(iter(G.V))

        stack = [v]
        output = []

        while stack:

            v = stack[-1]

            if G.deg(v) > 0:

                u = next(iter(G.neighbours(v)))

                stack.append(u)
                G.removeedge(u,v)  #removing the edges from our graph             

            else:

                output.append(stack.pop())

        return output


def eulerwalk(G):

    odds = [v for v in G.v if G.deg(v)%2 ]





if __name__ == "__main__":

    G = Graph([],"ab bc cd da bd be de".split())
    print(eulerTour_m2(G))

    # assert(isEulerian(G))
    # G.addvertex('d')
    # G.addedge('a','d')
    # assert(not isEulerian(G))