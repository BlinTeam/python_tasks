class MaxHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    @staticmethod
    def getParent(index):
        return (index - 1) // 2

    @staticmethod
    def getLeftChild(index):
        return 2 * index + 1

    @staticmethod
    def getRightChild(index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.getParent(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChild(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChild(index) < self.size

    def parent(self, index):
        return self.storage[self.getParent(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftChild(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChild(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def insert(self, data):
        for elem in data:
            self.size += 1 if not self.isFull() else 0
            self.storage[self.size - 1] = elem
            self.heapifyUp_rec(self.size - 1)

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parent(index) < self.storage[index]:
            self.swap(self.getParent(index), index)
            index = self.getParent(index)

    def heapifyUp_rec(self, index):
        if self.hasParent(index) and self.parent(index) < self.storage[index]:
            self.swap(self.getParent(index), index)
            self.heapifyUp_rec(self.getParent(index))

    def removeMax(self):
        if self.size == 0:
            raise Exception("Empty Heap")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown_rec(0)
        return data

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            biggerChild = self.getLeftChild(index)
            if self.hasRightChild(index) and \
                    self.rightChild(index) > self.leftChild(index):
                biggerChild = self.getRightChild(index)
            if self.storage[index] > self.storage[biggerChild]:
                break
            else:
                self.swap(index, biggerChild)
            index = biggerChild

    def heapifyDown_rec(self, index):
        biggest = index
        if self.hasLeftChild(index) and self.storage[biggest] < self.leftChild(index):
            biggest = self.getLeftChild(index)
        if self.hasRightChild(index) and self.storage[biggest] < self.rightChild(index):
            biggest = self.getRightChild(index)
        if biggest != index:
            self.swap(index, biggest)
            self.heapifyDown_rec(biggest)

    def constructHeap(self):
        for i in range(self.size):
            print(self.storage[i], " ")
        print("\n")
