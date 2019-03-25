
# Doubly Linked List (DL List) contains reference to the previous and next node and supports insertion and deletion in O(1) 
# if we are at the location we want to manipulate. Singly Linked List takes O(n) to remove the last element as it needs to
# traverse the whole list to update the previous to last pointer to tail.

# A node in a Doubly Linked List
class DListNode():

    def __init__(self, value=None, prev=None, next=None):
        self.value  = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.value)


class DoublyLinkedList():

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def addFirst(self, value):
        new_node = DListNode(value=value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = head
            # Change previous of head to new node
            self.head.prev = new_node
            # Move the head to point to the new node
            self.head = new_node

        self.size += 1

    def addLast(self, value):
        new_node = DListNode(value=value)
        if self.size = 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            # Update tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1

    def addAfter(self, value, prev_node):
        new_node = DListNode(value=value)

        new_node.next = prev_node.next
        new_node.prev = prev_node

        prev_node.next.prev = new_node
        prev_node.next = new_node

    def removeFirst(self):
        if self.size != 0:
            # Next element is first and points to None
            self.head.next.prev = None
            # Update head
            self.head = self.head.next
            size -= 1

    def removeLast(self):
        if self.size != 0:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            size -= 1

    def removeNode(self, node):

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        node.next = None
        node.prev = None
        size -= 1
    