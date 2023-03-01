


class Graph_K():

    def __init__(self,n):
        self.vertices = n
        self.graph = []

    def add_edge(self,u,v,weight):

        self.graph.append((u,v,weight))


    def find(self,u,parents):

        if parents[u] != u:

            parents[u] =self.find(parents[u],parents)

        return parents[u]


    def union(self,u,v,parents,ranks):

        pu = self.find(u,parents)
        pv = self.find(v,parents)

        if pu == pv:
            return False
        
        if ranks[pu] > ranks[pv]:

            parents[pv] = pu

        elif ranks[pv] > ranks[pu]:

            parents[pu] = pv

        else:

            parents[pv] = pu
            ranks[pu] +=1

        return True

    
    def kruskal_mst(self):

        mst = []
        # i = 0
        # e = 0

        self.graph = sorted(self.graph,key=lambda item: item[2])

        parents = list(range(self.vertices))
        ranks = [0]*(self.vertices)

        for u,v,weight in self.graph:

            if self.union(u,v,parents,ranks):

                mst.append((u,v,weight))

        return mst

if __name__ == '__main__':
	# g = Graph(4)
	# g.add_edge(0, 1, 10)
	# g.add_edge(0, 2, 6)
	# g.add_edge(0, 3, 5)
	# g.add_edge(1, 3, 15)
	# g.add_edge(2, 3, 4)

	# # Function call
	# print(g.kruskal_mst())

    g2 = Graph_K(6)
    g2.add_edge(0,1,4)
    g2.add_edge(1,2,2)
    g2.add_edge(0,2,4)
    g2.add_edge(2,5,2)
    g2.add_edge(2,3,3)
    g2.add_edge(2,4,4)
    g2.add_edge(3,4,3)
    g2.add_edge(4,5,3)

    print(g2.kruskal_mst())