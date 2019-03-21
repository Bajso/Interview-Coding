# HEAP data structure

# Although it might be intuitive to implement a Heap using a Node class, where each parent has a left and a right child,
# since Heap is a binary tree, instead, we can create it using an array. This makes it very compact.

# A MinHeap ensures that the minumum is always contained at root and that the value of every parent < children

# Parent - (index - 2) / 2
# Left Child - (index * 2) + 1
# Right Child - (index * 2) + 2

class MinIntHeap():

    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.items = []

    def getParentIndex(self, index):
        # floor division since 5 and 6 have same parent 2
        return (index - 1) // 2
    
    def getParent(self, index):
        return self.items[self.getParentIndex(index)]

    def getLeftChildsIndex(self, index):
        return index * 2 + 1

    def getLeftChild(self, index):
        return self.items[self.getLeftChildsIndex(index)]

    def getRightChildsIndex(self, index):
        return index * 2 + 2
    
    def getRightChild(self, index):
        return self.items[self.getRightChildsIndex(index)]

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildsIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildsIndex(index) < self.size

    def swap(self, indexOne, indexTwo):
        self.items[indexOne], self.items[indexTwo] = self.items[indexTwo], self.items[indexOne]

    # returns the value of root without removing
    def peek(self):
        assert self.size > 0
        return self.items[0]

    # removes and returns the root value
    def getMin(self):
        assert self.size > 0
        root = self.items[0]
        # assign last element to root
        self.items[0] = self.items.pop()
        self.size -= 1
        self.heapifyDown()
        return root

    # adds a new element
    def push(self, element):
        self.items.append(element)
        self.size += 1
        self.heapifyUp()

    # ensures order once the current root was removed
    def heapifyDown(self):
        index = 0
        
        # as heap is populated from left to right, if there in no left child then there is no right child
        while self.hasLeftChild(index):
            # get value of smallest child
            smaller_child_index = self.getLeftChildsIndex(index)
            if (self.hasRightChild(index) and self.getRightChild(index) < self.getLeftChild(index)):
                smaller_child_index = self.getRightChildsIndex(index)

            if self.items[index] > self.items[smaller_child_index]:
                self.swap(smaller_child_index, index)
            
            index = smaller_child_index

    # ensures order once a new element is added
    def heapifyUp(self):
        index = self.size - 1
        # as long as parent's value is smaller, swap
        while self.hasParent(index) and self.items[index] < self.getParent(index):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)     


heap = MinIntHeap()
heap.push(5)
heap.push(1)
heap.push(30)
heap.push(25)
heap.push(4)
heap.push(11)
heap.push(3)
heap.push(6)
heap.push(4)

print('Items:', heap.items, 'Size:', heap.size)

heap.getMin()
heap.getMin()
heap.getMin()
heap.getMin()
print('Items:', heap.items, 'Size:', heap.size)
