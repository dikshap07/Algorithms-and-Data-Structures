"""
find if a binary tree is symmetric
"""


"""
Solution: check if the tree is a mirror of itself and then if the left subtree is a mirror of right subtree and
right subtree is the mirror of left subtree and root is ewual

"""


def isMirror(node1,node2):

    if not node1 and not node2: #if both nodes None - true - leaf nodes but both equal
        return True

    if not node1 or not node2: return False #if either is None that means false both should have equal value

    return ( node1.val == node2.val  #va should be same
             and isMirror(node1.left,node2.right) #their children should be mirrors
             and isMirror(node1.right,node2.left)
    )


def isSymmetric(root):

    return isMirror(root,root)