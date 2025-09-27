from show_heap import show

class BinaryHeap:
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, node):
        self.heapList.append(node)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    # MinHeap
    def percUp(self, i):
        while i > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                newP = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = newP

            i = i // 2
 

def heapify(heapList, size):
    newHeap = BinaryHeap()
    
    for i in range(1, size + 1):
        newHeap.insert(heapList[i])
    
    return newHeap




oldHeap = [0, 99, 40, 25, 65, 12, 48, 18, 1, 98, 27, 7, 3, 45, 9, 30]
# oldHeap
newHeap = heapify(oldHeap, len(oldHeap) - 1).heapList

show(newHeap, len(newHeap) - 1)
    