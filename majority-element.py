from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] not in dict.keys():
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        print(dict)
        for i in dict:
            if dict[i] > len(nums) // 2:
                return i
            
    def majorityElement2(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in num_set:
            if nums.count(i) > len(nums) // 2:
                return i
                



nums = [3,2,3]
obj = Solution()
print(obj.majorityElement2(nums))