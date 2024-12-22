"""
Return True if there exists path btw 2 given node in a directed acyclic graph


"""

from collections import deque
"""
My intuition : we can just take the source node and start dfs from there, 
if we reach the destination node, then we return True
So in this scenerio, if we traverse thru all nodes like we did in our initial implementation, it wont be easy to find 
if path exists, BUT, we just just think of it as this way, if we use the given nodes and just traverse thru the nodes
 connected to those nodes, and dont find the destination node, that kinda means that the destinatin node does not have
  a path from source node i.e it is the disconnected node that we wouldnt have been able to reach if we just consider
   one source node in our dfsGraph function
   - we dont need to check if neighbour was already added cause its an acyclic graph
"""

#Time complexity : O(V) : space to store max all nodes; O(E): edges btw source and destinaton

def hasPath(graph, source, destination):

    stack = [source]

    while stack:
        curr_node = stack.pop()
        if curr_node == destination:return True

        for neighbour in graph[curr_node]:
            stack.append(neighbour)

    return False


def hasPathRec(draft,source,destination):

    #base case : when source -- destination\
    if source == destination: return True

    for neighbour in graph[source]:
        #since hasPathRec returns boolean
        if hasPathRec(graph,neighbour,destination): #checking for path btw neighbout and destination, if thats true
                                                    #we can return True
            return True
    return False


def hasPathBFS(graph, source, destination):
    queue = deque()
    queue.append(source)
    while queue:
        curr_node = queue.popleft()
        if curr_node == destination:return True
        for neighbour in graph[curr_node]:
            queue.append(neighbour)

    return False

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(hasPath(graph, 'f', 'k'))

edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
edges = [sorted(edge) for edge in edges]
print(edges)

adj_list = {}
for i in range(len(edges)):
    for edge in edges:
        if i == edge[0]:
            if i in adj_list:
                adj_list[i].append(edge[1])
            else:
                adj_list[i] = [edge[1]]

print(adj_list)