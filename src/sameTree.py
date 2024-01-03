

"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


def dfs_binary_tree(root,a=[]):#inorder traversal

    if not root:
        a.append("null")
        return a
    
    a.append(root.val)

    if not root.left and not root.right:
        return a
    
    dfs_binary_tree(root.left,a)
    dfs_binary_tree(root.right,a)

    return a

def isSameTree(p, q) -> bool:

    if (p and not q) or (not p and q):
        return False

    p_ = []
    q_ = []
    p_dfs = dfs_binary_tree(p,p_)
    # print(p_dfs)
    q_dfs = dfs_binary_tree(q,q_)
    # print(q_dfs)

    if len(p_dfs) == len(q_dfs):

        for i in range(len(p_dfs)):

            if p_dfs[i] != q_dfs[i]:
                return False
        
        return True

    return False

