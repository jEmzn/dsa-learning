class HashTable:

    def __init__(self):
        self.size = 5
        self.amount_data = 0
        self.slots = [None for i in range(self.size)]
        self.data = [None for i in range(self.size)]

    def put(self, key, value):

        hash_value = self.hashfunction(key)
        
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                next_slot = self.rehash(hash_value)
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value

                else:
                    self.data[next_slot] = value
        
        self.amount_data += 1

        loadf = self.load_factor(self.amount_data, self.size)
        if loadf > 0.7:
            self.resize(self.slots, self.data, self.size)

    def hashfunction(self, key):
        return key % self.size
    
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size
    
    def load_factor(self, amount, size):
        return amount / size

    def resize(self, slots, data, old_size):
        new_size = old_size * 2 + 1
        self.slots = [None for i in range(new_size)]
        self.data = [None for i in range(new_size)]
        self.size = new_size
        self.amount_data = 0

        for i in range(old_size):
            if slots[i] != None:
                self.put(slots[i], data[i])

        print("Resize complete!!")
        
    

h = HashTable()

# print((h.slots))
# [12, 44, 13, 88, 23, 94, 11, 39, 20, 16]
np = input().split()
while np[0] != "-1":
    h.put(int(np[0]), np[1])
    print(h.slots)
    print(h.data)
    print()
    np = input().split()
