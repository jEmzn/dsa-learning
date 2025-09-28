from show_heap import show

class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, node):
        self.heap_list.append(node)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, i):
        while i > 1:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def extract_min(self):
        min_node = self.heap_list[1]
        last_leaf = self.heap_list.pop()
        self.current_size -= 1
        self.heap_list[1] = last_leaf
        self.perc_down()

    def perc_down(self):
        # min_child = 
        pass

    def min_child(self, parent):
        pass


    
h = BinHeap()

n = int(input())

while n != 0:
    h.insert(n)
    show(h.heap_list, h.current_size)
    n = int(input())