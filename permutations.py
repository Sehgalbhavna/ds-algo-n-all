from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums):
            if len(nums) == 1:
                return [nums]
            
            res = []
            
            for i in range(len(nums)):
                anchor = [nums[i]]
                remaining = nums[:i] + nums[i + 1:]
                
                returned = backtrack(remaining)

                for result in returned:
                    res.append(anchor + result)
            
            return res
        
        return backtrack(nums)
    
    
obj = Solution()
nums = [1,2,3]
print(obj.permute(nums))
    