def subArray_sum(nums):
    c_sum = 0
    b_sum = float('-inf')
    for i in nums:
        if c_sum >= 0:
            c_sum += i
        else:
            c_sum = i
        print(c_sum)
        if c_sum > b_sum:
            b_sum = c_sum
            
    return b_sum
            

nums = [-2,-1]
result = subArray_sum(nums)
print(result)