from binary_tree import BinaryTree
from binary_heap import BinHeap


# r = BinaryTree('1')

# r.insertLeft('2')
# r.getLeftChild().insertLeft('4')
# r.getLeftChild().insertRight('5')
# r.insertRight('3')
# r.getRightChild().insertRight('6')

# print(r.inorder(r))
def buildHeap(alist):
        h = BinHeap()
        i = len(alist) // 2
        h.currentSize = len(alist)
        h.heapList = [0] + alist[:   ]
        while (i > 0):
            h.percDown(i)
            i = i - 1

        return h.heapList


aL = [4, 2, 7, 3, 5]

print(buildHeap(aL))







