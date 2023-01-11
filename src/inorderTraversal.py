class Tree():

    def __init__(self,val,left,right):

        self.val = val
        self.left = left
        self.right = right
    

class Solution():

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

            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)

        inorder(root)

        return nodes