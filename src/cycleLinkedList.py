class LinkedNode():

    def __init__(self,x):

        self.x = x
        self.next = None



#O(N)- TIME , O(1) Space soln: Floyd's cycle finding algo



def hasCycle(self, head):

    if not head:
        return False

    slow = head
    fast = head.next

    while fast != slow: #if they dont meet we are not in a cycle

        if fast is None or fast.next is None:
            return False #because we reached the tail

        slow = slow.next
        fast = fast.next.next #two steps ahead of slow

    # print(visited)
    return True



#O(N)- TIME , O(N) Space soln
def hasCycle(head):

    curr = head
    visited = []
    if not curr:
        return False


    while curr.next:

        if curr.next in visited:

            return True

        visited.append(curr)
        curr = curr.next


    return False


