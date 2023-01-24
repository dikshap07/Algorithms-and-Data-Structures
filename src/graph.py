class Graph():


    def __init__(self, V, E):

        """ V: set of vertices
        E : set of unordered pair of edges"""

        # self.V = set(V)  #so that we can take lists or sets or tuples as input, 
                            #since we are already storing vertices as keys we can remove this
        self.E = set((frozenset((u,v))) for u,v in E) 

        #to store _neighbours : we use a dictionary that maps vertices to sets of their _neighbours

        self._neighbours = {}


        for v in V:

            # self._neighbours[v] = set()  #putting this in a separate method
            self.addvertex(v)

        #for every vertex in an edge, we want to store the other end of that edge as the neighbour for that vertex

        for u,v in self.E:

            # self._neighbours[u].add(v)    #putting this in a separate method
            # self._neighbours[v].add(u)

            self.addedge(u,v)

    def addvertex(self,v):

        """
        To add a new vertex to the graph
        """

        if v not in self._neighbours:

            self._neighbours[v] = set()

    def addedge(self,u,v):

        """
        To add a new edge to the graph
        """

        self.addvertex(u)
        self.addvertex(v)
        self.E.add(frozenset([u,v]))
        self._neighbours[u].add(v)
        self._neighbours[v].add(u)

    def removeedge(self,u,v):

        """ 
        To remove an edge from the graph
        """
        e = frozenset([u,v])
        #need to remove it from E 

        if e in self.E:   #if the edge we are removing actually exists

            self.E.remove(e)

            # to remove from and _neighbours

            self._neighbours[u].remove(v)
            self._neighbours[v].remove(u)


    def removevertex(self,v):

        """
            To remove a vertex from the graph 
        """
        todelete = list(self.neighbours(v)) #we have to store separately because we are deleting from the set while iterating from it

        #removing the edges corresponding to the vertex v
        for u in todelete:  #we are using the method neighbours because it is in public interface

            self.removeedge(u,v)

        #removing the vertex        
        del self._neighbours[v]



    def deg(self,v):
        """

        Args:
            v (object): vertex

        Returns:
            int: degree of vertex v
        """
        # print(self._neighbours[v])
        return len(self._neighbours[v])


    def degree(self,v):   #degree of a vertex (Brute Force method when we dont have an adjacency list)

        """v: vertex iterates over edges and count increases by 1 if v is in that edge

        : Not a good way to calculate degree because loops over very edge in graph therefore to avoid
        that we should store _neighbours 
        """

        return sum(1 for e in self.E if v in e)

    def neighbours(self,v):

        return iter(self._neighbours[v])  #using iter makes sure nobody can change the private _neighbours

    @property #we make it a property so that we dont have to put () everytime we call method m
    def m(self):
        """

        Returns:
            int: Number of Edges
        """

        return len(self.E)

    @property

    def n(self):
        """

        Returns:
            int: Number of vertices
        """

        return len(self._neighbours)

if __name__ == "__main__":


    G = Graph([1,2,3],{(1,2),(2,3)})

    assert(G.deg(2) == 2 and G.deg(1) == 1)


    # print(f" Using Adjacency : G.deg(2) = {G.deg(2)}")
    # print(f" Using Brute Force : G.degree(2) = {G.degree(2)}")
    # print(list(G.neighbours(2)))
    # print(f"No of edges in G = {G.m}")
    # print(f"No of Vertices in G = {G.n}")

    assert(G.m == 2 and G.n == 3)

    G.removeedge(1,2)

    # print(f"No of edges in G = {G.m}")
    # print(f"No of Vertices in G = {G.n}")

    assert(G.m == 1 and G.n == 3)

    G.addedge(1,2)

    assert(G.m == 2 and G.n == 3)

    # print(f"No of edges in G = {G.m}")
    # print(f"No of Vertices in G = {G.n}")    

    G.removevertex(2)

    assert(G.m == 0 and G.n == 2)

    # print(f"No of edges in G = {G.m}")
    # print(f"No of Vertices in G = {G.n}")  

    print("Everything works fine!")