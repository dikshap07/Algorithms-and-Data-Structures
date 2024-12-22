"""
onnected_components_count, that takes in the adjacency list of an undirected graph.
The function should return the number of connected components within the graph.
"""


def connectedComponentsCount(graph):
    stack = []
    visited = set()

    connected_components = 0

    connected_components_list = []

    for node in list(graph.keys()):

        if node not in visited:
            stack.append(node)
            connected_components += 1
            components = []
            while stack:

                curr = stack.pop()

                if curr not in visited:
                    visited.add(curr)

                    components.append(curr)

                    for neighbour in graph[curr]:
                        if neighbour not in visited:
                            stack.append(neighbour)

            connected_components_list.append(components)

    return connected_components


def connectedComponentsCountRec(graph):
    seen = set()
    connected_components = 0

    def dfsRec(node, components):

        # base case : i.e. where recursion stops
        if node in seen:  # here this is where we want to stop the recursion cause adj list will never have an empty node
            return

        seen.add(node)
        components.extend([node])

        for neighbour in graph[node]:
            dfsRec(neighbour, components)  # we dont need to add the seen condition here bcz we do it at the top anyway
        return components

    connected_components_list = []
    for node in graph.keys():

        if node not in seen:
            components = []
            connected_components += 1
            components = dfsRec(node, components)
            connected_components_list.append(components)

    return connected_components


graph1 = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}


print(connectedComponentsCount(graph1))