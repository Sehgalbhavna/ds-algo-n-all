def can_rook_attack_one_another(rook_array):
    n = len(rook_array)   
    for row_i in range(n):
        row_count = 0
        for clo_i in range(n):
            row_count += rook_array[row_i][clo_i]
        if row_count > 1:
            return False
    for clo_i in range(n):
        clo_count = 0
        for row_i in range(n):
            clo_count += rook_array[row_i][clo_i]
        if clo_count > 1:
            return False
    return True
#test1
rook_array1 =[[1,0,0,0],
              [0,1,0,0],
              [0,0,0,1],
              [0,0,0,0]]
print(can_rook_attack_one_another(rook_array1))
print(can_rook_attack_one_another([[1]]))
#test2
rook_array2 =[[1,0],
              [1,0]]
print(can_rook_attack_one_another(rook_array2))

#test3
rook_array3 =[[0,0,1,0],
              [0,1,0,1],
              [0,0,0,1],
              [0,0,0,0]]
print(can_rook_attack_one_another(rook_array3))
