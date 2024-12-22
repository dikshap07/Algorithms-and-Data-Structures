"""
Find path of a node in a Binaty tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getPath(root,target):

    if not root: return []

    if root.val == target:
        return [root.val]

    left_path = getPath(root.left,target)
    if left_path:
        return [root.val] + left_path

    right_path = getPath(root.right,target)
    if right_path:
        return [root.val] + right_path

    return []


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

target = 5
path = getPath(root, target)
print("Path to node:", path)