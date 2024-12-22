class Graph:
    def __init__(self,adjacency_list=None):
        self.adjacency_list = adjacency_list if adjacency_list else []

    def add_edge(self, node, neighbor):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        self.adjacency_list[node].append(neighbor)

    def add_undirected_edge(self, node, neighbor):
        self.add_edge(node, neighbor)
        self.add_edge(neighbor, node)

    def get_graph(self):
        return self.adjacency_list



