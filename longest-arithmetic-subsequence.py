'''
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

 

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
'''

from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        length = len(nums)
        dict = [{} for i in range(length)]
        longest = 2
        for i in range(length):
            for j in range(i + 1, length):
                diff = nums[j] - nums[i]
                if diff in dict[i]:  # If i remembers same diff history count, j just stores the count + 1
                    dict[j][diff] = dict[i][diff] + 1
                else:
                    dict[j][diff] = 2 # Initialized as 2 because 2 numbers
                longest = max(longest,dict[j][diff])
        return longest

nums = [20,1,15,3,10,5,8]
obj = Solution()
print(obj.longestArithSeqLength(nums))