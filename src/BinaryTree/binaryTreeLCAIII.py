class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None



def getPath(self,node):

    path = [node]
    if not node.parent: return path

    while node.parent is not None:
        path.append(node.parent)
        node = node.parent

    return path

"""
Optimised soltuion

"""

def LCA(p,q):
    return








"""
O(h*2) + O(h) -> time complexity; O(h): space complexity - Passes but not optimised
"""
def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

    p_path = self.getPath(p)
    q_path = self.getPath(q)

    for node in p_path:
        if node in q_path:
            return node

    return None


