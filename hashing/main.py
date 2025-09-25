from hash_table import HashTable
from hash_table_qp import HashTableQP
from hash_table_ch import HashTableCh


h = HashTableCh(11)

h[10] = "cat"
h[22] = "dog"
h[31] = "lion"
h[4] = "cow"
h[15] = "bird"
h[28] = "goat"
h[17] = "tiger"
h[88] = "pig"
h[59] = "fish"

print(h.slots)
print(9/11)
print(h.get(59))


# print(h.data)