"""
DFS - go in one direction until you cant go further in that direction, and then switch
 - implemented using STACK i.e. Last in First Out

"""


from graph import Graph


# Create the graph
graph = Graph()

#here is a graph adjacency list
directed_graph1 = {
    'A': [ 'C','B'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

input_graph1 = Graph(directed_graph1)

graph2 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

input_graph2 = Graph(graph2)

"""
Iterative method
"""
def graphDFS(graph):

    stack = []
    seen = set()
    for node in graph.adjacency_list.keys():

        if node not in seen:

            stack.append(node)

            while stack:

                curr_node = stack.pop()
                if curr_node not in seen:
                    seen.add(curr_node)
                    print(curr_node)

                    stack.extend(neighbour for neighbour in graph.adjacency_list[curr_node] if neighbour not in seen)

    return

"""
Recursive method
"""


def graphDFSRec(graph):


    seen = set()

    def dfs(node):

        #base case : i.e. where recursion stops
        if node in seen: #here this is where we want to stop the recursion cause adj list will never have an empty node
            return

        seen.add(node)
        print(node)

        for neighbour in graph.adjacency_list[node]:
            dfs(neighbour) #we dont need to add the seen condition here bcz we do it at the top anyway

    for node in graph.adjacency_list.keys():

        if node not in seen:

            dfs(node)

    return









graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# graphDFS(graph)

print(f" iterative : {graphDFS(input_graph1)}")
print(f" recursive : {graphDFSRec(input_graph1)}")