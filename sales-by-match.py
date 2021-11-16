def salesByMatch(arr1):
    count = 0
    colorset1 = set({})
    if len(arr1) <= 1:
        return 0
    for i in range(len(arr1)):
        if arr1[i] in colorset1:
            count += 1
            colorset1.remove(arr1[i])
        else:
            colorset1.add(arr1[i])
    return count


arr1 = [10,20,20]
print(salesByMatch(arr1))