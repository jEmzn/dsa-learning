from show_heap import show

class MinHeap:

    def __init__(self):
        # self.heapList = [0]
        # self.heapList = [0, 1, 1, 2, 3, 7]
        self.heapList = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
        self.currentSize = 10

    def insert(self, num:int):
        self.heapList.append(num)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                p = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = p
            else:
                break

            i = i // 2

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            minC = self.minChild(i)
            if self.heapList[i] > self.heapList[minC]:
                p = self.heapList[minC]
                self.heapList[minC] = self.heapList[i]
                self.heapList[i] = p
            
            i = minC

    def extract_min(self):
        rVal = self.heapList[1]
        if self.currentSize > 1:
            self.heapList[1] = self.heapList.pop()
            self.currentSize = self.currentSize - 1
            self.percDown(1)
        elif self.currentSize == 1:
            self.heapList.pop()
            self.currentSize = self.currentSize - 1
        return rVal

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2 + 1] < self.heapList[i * 2]:
                return i * 2 + 1
            else:
                return i * 2

    def peek(self):
        if self.heapList[1]:
            return self.heapList[1]
        return None
    
    def size(self):
        return self.currentSize
    
    def empty(self):
        return self.currentSize == 0


h = MinHeap()

# h.insert(2)
# print(h.heapList)
# h.insert(5)
# print(h.heapList)
# h.insert(1)
# print(h.heapList)
show(h.heapList, h.currentSize)
print(h.extract_min())
show(h.heapList, h.currentSize)
# print(h.heapList)