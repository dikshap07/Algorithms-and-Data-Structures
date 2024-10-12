"""
Find LCA of 2 nodes in Binary Tree
"""
#O(n) - time complexity
def LCA(root,p1,p2):

    if not root or root == p1 or root == p2:  # we stop if either of p1 and p2 are at root, cause then we dont need to go further
        return root

    left_sub = LCA(root.left,p1,p2) #check the left subtree for targets, if found we will return the target that was found
    right_sub = LCA(root.right,p1,p2) #check the right subtree for targets, if found we will return the target that was found


    if not left_sub and not right_sub: return root #if target wasnt found in both, then root is the target, because targets have to exist in the tree

    if not left_sub: return right_sub #return the non null value btw left and right
    elif not right_sub: return left_sub
    else:
        return root

