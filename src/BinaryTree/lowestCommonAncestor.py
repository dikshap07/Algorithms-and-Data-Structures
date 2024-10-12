"""
Find LCA of 2 nodes in Binary Tree
"""
#O(n) - time complexity
def LCA(root,p1,p2):

    if not root or root == p1 or root == p2:
        return root

    left_sub = LCA(root.left,p1,p2)
    right_sub = LCA(root.right,p1,p2)


    if not left_sub and not right_sub: return root

    if not left_sub: return right_sub
    elif not right_sub: return left_sub
    else:
        return root

