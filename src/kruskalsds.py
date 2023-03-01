"""Implementing Kruskal's algorithm using Disjoint sets."""

class DisjointSets():

    def __init__(self,n): #n:num of vertices/nodes

        self.parent = list(range(n))
        self.rank = [0]*n #rank of each vertex initially will be 0

    #find the root of the set containing u
    def find(self,u):

        if self.parent[u] != u:   #if the u is not the parent node

            #using path compressions set parent of each node in the cluster to be the root node
            self.parent[u] = self.find(self.parent[u])  #find the parent of u's parent
            print(f"{u}'s parent: {self.parent[u]}" )

        return self.parent[u]  # we can return this because now parent of u is the root of the disjoint set

    
    def union(self,u,v):

        print("rank og ",self.rank)
        print("parent og",self.parent)
        print(f" u: {u} and  v : {v}" )

        pu = self.find(u)
        pv = self.find(v)
        print(f"parent of u : {pu} and parent of v: {pv}" )

        if pu == pv:  #if root of both is same they are already in the same set
            print("cannot perform union since they are already in the same family")
            return False

    

        if self.rank[pu] > self.rank[pv]:

                self.parent[pv] = pu  #parent of root v is now parent of root of u

        elif self.rank[pu] < self.rank[pv]:

                self.parent[pu] = pv #parent of root v is now parent of root of v

        else:

            self.parent[pv] = pu
            self.rank[pu] += 1

            print("rank",self.rank)
            print("parent",self.parent)

        return True

def kruskal(edges, n):
    
    edges.sort()  #first sort the edges of the graph

    dsu = DisjointSets(n)

    mst = []  #to store the final mst

    for weight, u, v in edges: #for all the edges in ascending order add to mst if it doesnt produce a cycle

        if dsu.union(u, v):
            mst.append(( weight, u, v))

    return mst


n = 5
edges = [(10, 0, 1), (6, 0, 2), (5, 0, 3), (15, 1, 3), (4, 2, 3)]

mst = kruskal(edges, n)
print(mst)



