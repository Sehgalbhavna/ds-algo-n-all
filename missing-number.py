from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        map_nums = set(nums)
        for i in range(1,len(nums)+1):
            if i not in map_nums:
                print(i)
                return i
            
    def missingNumber2(self, nums: List[int]) -> int:
        map_nums = {}
        for i in nums:
            if i not in map_nums:
                map_nums[i] = True
        for i in range(1,len(nums)+1):
            if i not in map_nums:
                return i
    
    def missingNumber3(self, nums: List[int]) -> int:
        return sum(nums) - (len(nums))*(len(nums) + 1)//2
    
obj1 = Solution()
nums = [1,2,4,5,6]
result = obj1.missingNumber3(nums)
print(result)