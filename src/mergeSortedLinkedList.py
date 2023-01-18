class ListNode():

    def __init__(self,val):

        self.val = val
        self.next = next


#iteraive soln

def mergeSortedLinkedList(l1,l2):  

    prehead = ListNode(-1)  #pointer to the fnal sorted ll header

    prev = prehead  #at the first iteration of loop prehead.next will be assigned

    while l1 and l2:  #until lls are not none

        if l1.val < l2.val:

            prev.next = l1
            l1 = l1.next

        else:

            prev.next = l2
            l2 = l2.next

        prev = prev.next

    
    prev.next = l1 if l1 is not None else l2

    return prehead.next


#Recursive soln


def mergeSortedLinkedList(l1,l2):  

    if not l1:return l2

    if not l2: return l1

    elif l1.val < l2.val:

        l1.next = mergeSortedLinkedList(l1.next,l2)
        return l1

    else:

        l2.next = mergeSortedLinkedList(l1,l2.next)
        return l2
 
