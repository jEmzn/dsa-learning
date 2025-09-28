class BinaryHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                t = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = t
            i = i // 2

    def insert(self, val):
        self.heapList.append(val)
        self.currentSize = self.currentSize + 1
        if self.currentSize > 0:
            self.percUp(self.currentSize)


# class Solution:
#     def findKthLargest(self, nums, k: int) -> int:
#         pass

h = BinaryHeap()

num = int(input())

while num != 0:
    h.insert(num)
    print(h.heapList)
    num = int(input())

