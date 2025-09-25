# Linear Prop

class HashTableCh:
    def __init__(self, size=10):
        self.size = size
        self.slots = [[] for i in range(size)]
        self.data = [[] for i in range(size)]

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # Replace
            else:
                self.rehash(hashvalue, key, data)
                # while self.slots[nextslot] != None and \
                #         self.slots[nextslot] != key:
                #     nextslot = self.rehash(nextslot, len(self.slots))

                # if self.slots[nextslot] == None:
                #     self.slots[nextslot] = key
                #     self.data[nextslot] = data
                # else:
                #     self.data[nextslot] = data  # Replace

    # Hash function
    def hashfunction(self, key, size):
        return key % size
    
    def rehash(self, oldhash, key, data):
        # return (oldhash + 1) % size
        self.slots[oldhash].append(key)
        self.data[oldhash].append(data)
    
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        for i in range(len(self.slots[startslot])):
            if self.slots[startslot][i] == key:
                return self.data[startslot][i]
            
        return None

        # data = None
        # stop = False
        # found = False
        # position = startslot
        # while self.slots[position] != None and \
        #         not found and not stop:
        #     if self.slots[position] == key:
        #         found = True
        #         data = self.data[position]
        #     else:
        #         position = self.rehash(position, len(self.slots))
        #         if position == startslot:
        #             stop = True
        # return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)
        