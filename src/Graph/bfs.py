"""
BFS for a grapg
-implemented using QUEUE i.e. first in first out
- only implemented iteravtively
"""

from graph import Graph
from collections import deque


def bfsGraph(graph):

    queue = deque()
    seen = set()


    for node in graph.adjacency_list.keys():

        if node not in seen:
            queue.append(node)

            while queue:

                curr_node = queue.popleft()

                if curr_node not in seen:

                    seen.add(curr_node)
                    print(curr_node)

                    queue.extend(neighbour for neighbour in graph.adjacency_list[curr_node] if neighbour not in seen)

    return


directed_graph1 = {
    'A': [ 'C','B'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

input_graph1 = Graph(directed_graph1)
bfsGraph(input_graph1)