def second_largest_element(element_list):
    largest = None
    second_largest = None
    for element in element_list:
        print(largest,second_largest)
        if largest == None:
            largest = element
            #print(largest)
        elif element > largest:
            second_largest = largest
            #print(second_largest)
            largest = element
            #print(largest)
        elif second_largest == None:
            second_largest = element
            #print(second_largest)
        elif element > second_largest:
            #print(element)
            second_largest = element
    return second_largest

list1 = [1,3,4,5,0,2]       
print(second_largest_element(list1))
list2 = []
#print(second_largest_element(list2))
list3 = [1]
#print(second_largest_element(list3))
list4 = [1,2,2]
#print(second_largest_element(list4))
