#Using map
def repate_missing_number(nums):
    max = len(nums)
    map_nums = {}
    result = {}
    for i in nums:
        if i not in map_nums:
            map_nums[i] = True
        else:
            result["repate"] = nums[i]
    for i in range(1,max+1):
        if i not in map_nums:
            result["missing"] = i
    return result

def missingNumber(nums):
    n = len(nums)
    total = ((n+1) * n ) // 2   
    for i in nums:
        total -= i
    return total


def findDuplicate(nums):
    map = {}
    for i in nums:
        if i not in map:
            map[i] = True
        else:
            return i

nums = [ 4, 3, 6, 2, 1, 1 ]
response = repate_missing_number(nums)
print(response)
print(repate_missing_number([0,1,3]))
print(findDuplicate(nums))
        