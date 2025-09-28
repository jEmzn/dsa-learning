def show(heapList, size):
    subH = subLevel(heapList, size)
    heapLevel = len(subH) - 1
    print(heapList)
    
    for level in range(0, heapLevel + 1):
        sp = heapLevel-level + 1
        gap = " "*(2*((2**sp-1)*2+1))
        print(f"{" "*(2*(2**sp-1))}{gap.join(list(map(changeDigit, subH[level])))}")