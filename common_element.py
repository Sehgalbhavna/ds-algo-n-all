def common_elements(arr1,arr2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 2
            print(result)
        elif arr1[p1] > arr2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result            
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).
print(common_elements(list_a1, list_a2))
list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).
print(common_elements(list_b1, list_b2))
list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_b1, list_b2) should return [] (an empty list).
print(common_elements(list_c1, list_c2))