'''

'''


from typing import List
class Solution:
    
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dict = {}
        lowest = 0
        
        if len(nums) == 0:
            return nums
        
        for i in range(len(nums)):
            if nums[i] not in dict.keys():
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1  
                   
        for i in dict:
            if dict[i] == 1:
                return i

    def singleNonDuplicate2(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if (nums[m] == nums[m + 1]) ^ (m % 2):
                i = m + (m % 2)
            else:
                j = m - (m % 2)
        m = i

        return nums[m]
    
    '''
    Binary Search on Evens Indexes Only
    f it is, then we know that mid is not the single element, and that the single element must be at an even index after mid. Therefore, we set lo to be mid + 2. It is +2 rather than the usual +1 because we want it to point at an even index.
    If it is not, then we know that the single element is either at mid, or at some index before mid. Therefore, we set hi to be mid.
    Once lo == hi, the search space is down to 1 element, and this must be the single element, so we return it.
    '''

    def singleNonDuplicate3(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]

nums = [3,7,7,10,10,11,11]
obj = Solution()

print(obj.singleNonDuplicate3(nums))
#print(obj.singleNonDuplicate2(nums))