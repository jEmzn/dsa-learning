# Quadratic Probing

class HashTableQP:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # Replace
            else:
                rehash_count = 1
                nextslot = self.rehash(hashvalue, rehash_count, len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, rehash_count, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # Replace

    # Hash function
    def hashfunction(self, key, size):
        return key % size
    
    def rehash(self, oldhash, count, size):
        # return (oldhash + 1) % size
        return (oldhash + (count**2)) % size
    
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                rehash_count = 1
                position = self.rehash(position, rehash_count, len(self.slots))
                if position == startslot:
                    stop = True

        return data
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)