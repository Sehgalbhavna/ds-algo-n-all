from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
    
nums = [3,2,2,3]
val = 3

obj = Solution()
print(obj.removeElement(nums,val))