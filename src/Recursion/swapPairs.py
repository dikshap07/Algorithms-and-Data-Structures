
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):

    if not head or not head.next:
        return head

    
    first = head
    second = head.next
    prev_node = ListNode(-1)
    head_ = second

    while first:

        if first.next is None:

            break

        second = first.next

        tmp_node = second.next   #third

        first.next = tmp_node  #first->third
        second.next = first   #second-> first

        
        prev_node.next = second
        prev_node = first
        first = tmp_node

    return head_




    