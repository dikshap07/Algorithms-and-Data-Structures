class BinaryTree:

    def __init__(self,value):

        self.val = value
        self.left = None
        self.right = None
        self.parent = None
    



#iterative soln

def inOrderTraversel_iter(root):

    currentNode = root
    nodes = []
    stack = []


    while currentNode or stack:

        while currentNode:

            stack.append(currentNode)
            currentNode = currentNode.left

        currentNode = stack.pop()

        nodes.append(currentNode.val)

        currentNode = currentNode.right

    return nodes
    

#recursive soln


def inOrderTraversel_recur(root):

    nodes = []


    def inorder(root):

        if not root:
            return 

        inorder(root.left)
        nodes.append(root.val)
        inorder(root.right)

    inorder(root)

    return nodes


#Constructing Binary Tree
bt = BinaryTree(1)
bt.parent = None
bt.left = BinaryTree(2)
bt.right = BinaryTree(3)
bt.left.parent = bt
bt.right.parent = bt
bt.left.left = BinaryTree(4)
bt.left.left.parent = bt.left
k = bt.left.left
k.right = BinaryTree(8)
k.right.parent = k
bt.right.left = BinaryTree(6)
bt.right.right = BinaryTree(7)
l = bt.right 
l.right.parent = l
l.left.parent = l

print(f" inOrder using iteration : {inOrderTraversel_iter(bt)}")
print(f" inOrder using Recursion : {inOrderTraversel_recur(bt)}")