def sortAnArray(arr):
    l = len(arr)
    count_0 = count_1 = count_2 = 0
    
    for i in range(l):
        if arr[i] == 0:
            count_0 += 1
        elif arr[i] == 1:
            count_1 += 1
        else:
            count_2 += 1
    print(count_0,count_1,count_2)
    i = 0
    while i < l:
        if count_0 != 0:
            arr[i] = 0
            print(arr[i])
            count_0 -= 1
            i += 1
        elif count_1 != 0:
            arr[i] = 1
            count_1 -= 1
            i += 1
        elif count_2 != 0:
            arr[i] = 2
            count_2 -= 1
            i += 1
    print(arr)
    return arr

def sortColors(nums):
    colors = [0, 0, 0]
        
    for color in nums:
        colors[color] += 1
            
    pointer = 0
    print(colors)
    for index in range(3):
        while colors[index] > 0:
            nums[pointer] = index
            pointer += 1
            colors[index] -= 1
    print(nums)
            
arr = [1,2,0,0,1,0,2]
sortColors(arr)
        
