def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1

def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]
        
        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index -1
    return -1
        
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]   
    if mid_number == number_to_find:
        return mid_index
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def binary_search_all_indexes(number_list, number_to_find):
    index = binary_search(number_list, number_to_find)
    indices = [index]
    i = index - 1
    while i >= 0:
        if number_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i -= 1
    
    i = index + 1
    while i < len(number_list):
        if number_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i += 1
    return sorted(indices)
    
         
    
   
    
if __name__ == '__main__':
    # numbers_list = [1,4,6,9,10,5,7]
    # number_to_find = 5
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15  
    index = binary_search_all_indexes(numbers_list, number_to_find)
    print(f"Number found at index {index}")