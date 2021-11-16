#### Write a Python program to calculate the sum of a list of numbers
def sum_list_number(list):
    size = len(list)
    if size == 1:
        return list[0]
    return list[0] + sum_list_number(list[1:])

def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)
 
def integer_to_string(int):
    str1 = ''
    while int != 0:
        str1 += str(int%10)
        int = int // 10
    return str1[::-1] 

def to_string_to_base(num,base):
    c_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if num < base:
        return c_string[num]
    else:
        return to_string_to_base(num // base, base)  + c_string[num % base]

def list_sum_recursive(list1):
    sum = 0
    if len(list1) == 1:
        return list1[0]
    
    for item in list1:
        itemsize = 0
        if type(item) is list:
            sum += list_sum(item)
        else:
            sum += item
    return sum

def list_sum(list1):
    size = len(list1)
    sum = 0
    if size == 0:
        return list1[0]
    for item in list1:
        if type(item) is list:
            for i in item:
                sum += i
        else:
            sum += item
    return sum    

if __name__ == '__main__':
    Test_Data =[1, 2, [3,4], [5,6]]
    print(list_sum_recursive(Test_Data))
    # list1 = [11, 5, 17, 18, 23]
    # total1 = sumOfList(list1, len(list1))
    # print(total1)
    # total2 = sum_list_number(list1)
    # print(total2)
    # int1 = 1289
    # print(to_string_to_base(4, 2))

    