from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1, -1]
        
        start = self.binarySearch(nums, target, True)
        end = self.binarySearch(nums, target, False)
        return [start,end]
    
    def binarySearch(self, nums, target, leftBias):
        l , r = 0 , len(nums) - 1
        print(l , r)
            
        while l <= r:
            mid = (l + r) // 2
                
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                i = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1
        return i

obj = Solution()
nums = [5,7,7,8,8,10]
target = 8

print(obj.searchRange(nums,target))
                

        