
def show(heapList, size):
    subH = subLevel(heapList, size)
    heapLevel = len(subH) - 1
    print(heapList)
    
    for level in range(0, heapLevel + 1):
        sp = heapLevel-level + 1
        gap = " "*(2*((2**sp-1)*2+1))
        print(f"{" "*(2*(2**sp-1))}{gap.join(list(map(changeDigit, subH[level])))}")

def changeDigit(num):
    return f"{num:2d}"

def subLevel(heapList, size):
    alist = [[heapList[1]]]
    i = 2
    # size = len(list) - 1
    while i + 2 <= size:
        # print(list[i:i * 2])
        alist.append(heapList[i:i*2])
        i = i * 2
    # print(list[i:])
    if i <= size:
        alist.append(heapList[i:])
    return alist


# def checkLevel(heapList):
#     level = 0
#     total = 0
#     while total + 2**level < len(heapList):
#         total += 2**level
#         level = level + 1
#     return level

def setText(alist, level):
    sp = 0
    for i in range(level):  # 1 3 7 15 31
        sp = sp*2 + 1
    pass




# heapList = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
# heapList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(subLevel(heapList, 10))
# show(heapList, 10)

# j = 5
# for i in range(j):
#     print(f"{" "*(2*j-2*i)}{"*"*(i*4+1)}")

#               5
#       9              11
#   14      18      19      21