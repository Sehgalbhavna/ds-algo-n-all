'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            print(i)
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = i
            if (target - nums[i]) in nums_dict and nums_dict[(target - nums[i])] != i:
                 return [nums_dict[(target - nums[i])], i]

    
    def twoSum1(self, nums: List[int], target: int) -> bool:
        issum_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in issum_dict:
                issum_dict[nums[i]] = i
            if (target - nums[i]) in issum_dict and issum_dict[target - nums[i]] != i:
                return True
        return False
                
            
obj = Solution()
#Test 1
nums = [2,7,11,15]
target = 9    
response = obj.twoSum1(nums, target)
print(response)

#Test 2
nums1 = [3,2,1]
target1 = 6    
response = obj.twoSum1(nums1, target1)
print(response)

#Test 3
nums2 = [3,3]
target2 = 6    
response = obj.twoSum(nums2, target2)
print(response)