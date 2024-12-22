"""

shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B).
The function should return the length of the shortest path between A and B. Consider the length as the number of
edges in the path, not the number of nodes. If there is no path between A and B, then return -1. You can assume
 that A and B exist as nodes in the graph.

 BFS: is a better idea here, cause dfs might lead us to unnecessary nodes before we reach destination
"""

from collections import deque

graph1 = {
"w":["x","v"],
    "x": ["w","y"],
    "y":["x","z"],
    "v":["w","z"],
    "z":["y","v"]
}

#Time complexity : O(V+E): because worst case it will go thru all nodes and edges

#since BFS will gaurantee that the first time we reach nodeB would be the shortest distance we can also just stop as soon as we reach nobe B

def getShortestPath(graph,nodeA,nodeB):

    visited = set()
    queue = deque()
    queue.append([nodeA,0])
    paths = []
    shortest_path = float("inf")
    while queue:

        curr_node,dist = queue.popleft()

        if curr_node == nodeB:
            shortest_path = min(shortest_path,dist)
            paths.append([curr_node,dist])
            return dist #we exit as soon as we reach nodeB the first time


        if curr_node not in visited:
            # if curr_node != nodeB: #we dont need this, because if it adds nodeB, that means we gauranteed got atleast the shortest path
            visited.add(curr_node)
            for neighbour in graph[curr_node]:

                if neighbour not in visited:
                    queue.append([neighbour,dist+1])

    print(paths)
    return -1 #because we would have already exited if we found nodeB
        # shortest_path) if shortest_path != float("inf") else -1



print(getShortestPath(graph1,"w","z"))





