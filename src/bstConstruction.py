class BST:

    def __init__(self,value):

        self.value = value
        self.left = None
        self.right = None


#using iterative method


#Average : O(log(n)) time | O(1) space
#worst : O(N) time | O(1)   space

    def insert(self,value):  

        #initialize a variable that keeps track of what node we are at
        currentNode = self # because in the beginning the current node is the node where we start our insertion and that is self

        while True:

            if value < currentNode.value:

                #check if left node from here is an actual BST or the end

                if currentNode.left is None:#we create a left subtree

                    currentNode.left = BST(value)   #if none we are adding the value that we are trying to insert 
                    break                                #at this left node

                else:#make left node of current node so that we can now check for its child nodes

                    currentNode = currentNode.left   #assigning our currentNode to the left subtree


            else:    #to check the right sub tree for insertion

                if currentNode.right is None:

                    currentNode.right = BST(value)
                    break
            
                else:

                    currentNode = currentNode.right
                


        return self   #so that we can chain the output

    
    

    #Average : O(log(n)) time | O(1) space
    #worst : O(N) time | O(1)   space
    
    def contains(self,value):

        currentNode = self

        while currentNode is not None:

            if value < currentNode.value:


                currentNode = currentNode.left


            elif value > currentNode.value: 

                currentNode = currentNode.right

            else:

                return True

        return False

    def getMinValue(self):

        currentNode = self

        

            
        while currentNode.left is not None:

            currentNode = currentNode.left

        return currentNode.value
        


    #Average : O(log(n)) time | O(1) space
    #worst : O(N) time | O(1)   space



    def remove(self,value,parentNode = None):

        currentNode = self

        print(currentNode.value)
        print(value)
        
        while currentNode is not None:


            if value < currentNode.value:

                parentNode = currentNode

                currentNode = currentNode.left

            elif value > currentNode.value:

                parentNode = currentNode

                currentNode = currentNode.right

            else:  #when we have found the value that we need to delete


        #case1 : if the node has both left and right child nodes

                if currentNode.left is not None and currentNode.right is not None:

                    print('both child found for ', currentNode.value)

                    currentNode.value = currentNode.right.getMinValue()

                    #currentNode.value = smallest value of the right sub tree

                    #when we find the left most value in the right sub tree we remove it

                    currentNode.right.remove(currentNode.value,currentNode)   #because here our BST is the right 
                                                                            #tree as in currentNode.right thatys
                                                                            #we are using currentNode.right.remove()

        #case2 : when doesnt have 2 child nodes present

        #case2.1 : when node is the root node or doesnt have a parent and only has one child (the above will only work when root node has both child nodes that is why we need it)
        
                elif parentNode is None:   
                    if currentNode.left is  not None:

                        print('Root node only has left child')

                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left

                    elif currentNode.right is not None:

                        print('Root node only has right child')


                        currentNode.value = currentNode.right.value            
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right  #at last so that we dnt replace og without using it first

                    else:

                        currentNode.value = None #discuss with interviewer as this means we are deleting the BST'''

            #case2.2 : when node had a parent
                elif parentNode.left == currentNode:  #if current node is the left child of its parent node

                    print('if node is left')

                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right   #doesnt just rpelace value efficiently rpelaces the whole sub tree
                    #above line means the left child of parent will be assigned currentNode.left is the current
                    #node has a left child otherwise it will be assigned the right child of the currentNode

                elif parentNode.right == currentNode:

                    print('if node is right')

                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right

                break

        
        return self

