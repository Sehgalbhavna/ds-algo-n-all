
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {}
        l = len(nums)
        sum = 0
        subarray_sum = 0

        for num in nums:
            sum += num
            if sum == k:
                subarray_sum += 1
            if sum - k in hash_map:
                subarray_sum += hash_map[sum - k]    
            if sum in hash_map:
                hash_map[sum] += 1
            else:
                hash_map[sum] = 1

        return subarray_sum