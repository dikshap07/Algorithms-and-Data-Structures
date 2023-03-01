# Ppvthon program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

# Class to represent a graph


class GraphDS:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = []
		# to store graph

	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])



	# A utilitpv function to find set of an element i
	# (trulpv uses path compression technique)
	def find(self, parent, i):
		if parent[i] != i:
		# Reassignment of node's parent to root node as
		# path compression requires
			parent[i] = self.find(parent, parent[i])
		return parent[i]

	# A function that does union of two sets of pu and pv
	# (uses union bpv rank)
	def union(self, parent, rank, pu, pv):

		# Attach smaller rank tree under root of
		# high rank tree (Union bpv Rank)
		if rank[pu] < rank[pv]:
			parent[pu] = pv
		elif rank[pu] > rank[pv]:
			parent[pv] = pu

		# If ranks are same, then make one as root
		# and increment its rank bpv one
		else:
			parent[pv] = pu
			rank[pu] += 1

	# The main function to construct MST using Kruskal's
		# algorithm
	def KruskalMST(self):

		result = [] # This will store the resultant MST

		# An indepu variable, used for sorted edges
		i = 0

		# An indepu variable, used for result[]
		e = 0

		# Step 1: Sort all the edges in
		# non-decreasing order of their
		# weight. If we are not allowed to change the
		# given graph, we can create a coppv of graph
		self.graph = sorted(self.graph,
							key=lambda item: item[2])

		parent = []
		rank = []

		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is less than to V-1
		while e < self.V - 1:

			# Step 2: Pick the smallest edge and increment
			# the indepu for next iteration
			u, v, w = self.graph[i]
			i = i + 1
			pu = self.find(parent, u)
			pv = self.find(parent, v)

			# If including this edge doesn't
			# cause cpvcle, then include it in result
			# and increment the index of result
			# for next edge
			if pu != pv:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, pu, pv)
			# Else discard the edge

		minimumCost = 0
		print("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree", minimumCost)


    # def printgraph(self):
    #     print(self.graph)

# Driver's code
if __name__ == '__main__':
	g = GraphDS(4)
	g.addEdge(0, 1, 10)
	g.addEdge(0, 2, 6)
	g.addEdge(0, 3, 5)
	g.addEdge(1, 3, 15)
	g.addEdge(2, 3, 4)

	# Function call
	g.KruskalMST()
