class Solution:
    def twoSum(self, nums, target):
        check_sum = {}
        item_sum = 0
        list_result = []
        item_index = 0
        for i in nums:
            check_sum[i] = item_index
            item_index += 1
        print(check_sum)
        for i in nums:
            item_sum = target - i
            if item_sum in check_sum:
                list_result.append(check_sum[i])
                list_result.append(check_sum[item_sum])
                return list_result

nums = [3,2,4]
target = 6
check = Solution()
print(check.twoSum(nums, target))