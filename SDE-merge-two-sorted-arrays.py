def mergeTwoSortedArray(ar1, ar2):
    swap = False
    temp = 0
    for i in ar1:
        for j in ar2:
            if ar1[i] > ar2[j]:
                temp = ar1[i]
                ar1[i] = ar2[j]
                ar2[j] = temp
                swap = True
        if swap is True:
            break
    ar2.sort()
ar1 = [10]
ar2 = [2,3]
mergeTwoSortedArray(ar1, ar2)
print(ar1)
print(ar2)