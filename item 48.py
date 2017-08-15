listA = [67, 45, 2, 13, 1, 998]

listB = [89, 23, 33, 45, 10, 12, 45, 45, 45]

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(listA)
print(listA)
bubbleSort(listB)
print(listB)
