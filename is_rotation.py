def is_rotation(list1, list2):
    rotation = False
    if len(list1) == len(list2):
        for i in list1:
            if list1[i] in list2:
                rotation = True
            else:
                rotation = False
    return rotation

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]

print(is_rotation(list1, list2a))

list2b = [4, 5, 6, 7, 1, 2, 3]
print(is_rotation(list1, list2b))