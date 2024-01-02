
#DFS Using Stack



def dfs_stack(starting_node):

    stack = []
    dfs_order = []
    visited = set()   #adding record of visited to ensure not going into infinite loop in a complex graph
    stack.append(starting_node)

    while stack:

        current_node = stack.pop()
        # print(stack)
        dfs_order.append(current_node.name)
        # print(dfs_order)
        visited.add(current_node)
        if current_node in visited:
            continue

        #look for neighbours of current_node

        for child in current_node.children:

            if child and child not in visited:

                stack.append(child)

    return dfs_order

def dfs(root,a= []):
    if root is None:
        return

    a.append(root.name)

    for child in root.children:
        if child:
            dfs(child,a)

    return a

#building graph
class Node():

    def __init__(self,name):
        self.name = name
        self.children = []


    def add_child(self,name):
        self.children.append(Node(name))



tree = Node('A')   #root node for our tree/graph
tree.add_child('B')  #adding children of A
tree.add_child('C')
tree.add_child('D')
tree.children[0].add_child('E')    #adding children of B
tree.children[0].add_child('F')
tree.children[2].add_child('G')   #adding children of D
tree.children[2].add_child('H')

B = tree.children[0]
B.children[1].add_child('I')
B.children[1].add_child('J')

#adding children of 'G'

D = tree.children[2]
D.children[0].add_child('K')

print(dfs(tree))