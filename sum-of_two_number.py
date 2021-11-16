def sum_of_two(given_array, number_sum):
    number_seen = {}
    for item in given_array:
        if(number_sum - item) in number_seen:
            print(str((number_seen - item)) + "," + str(item))
            return
        else:
            number_seen[item] = 1
    print("there is no pair that adds up to "+ number_sum)

arr1 = [3, 4, 1, 2, 9]
item = 10
print(sum_of_two(arr1,item))