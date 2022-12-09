"""
DEFINITION: Doubly linked lists are different from singly linked lists because
there are two pointers, the next pointer and the previous pointer. The next 
pointers are connecting the nodes forward, while the previous pointer is 
connecting the nodes backwards. 
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes for edge cases
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    """
    ADDITION: To add a listnode to a doubly linked list, you would assign the next
    pointer of the node before it to refer to the target listnode, and the target's 
    previous pointer to refer to the node before it.
    """
    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

"""
REMOVING: To remove the last node of a doubly linked list, we only need a pointer
to the tail because from our tail we can follow our previous pointer to take us
to 
"""
