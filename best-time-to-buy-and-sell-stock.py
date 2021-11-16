
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = 0
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                    maxprofit = max(maxprofit,profit)
        return maxprofit
    
    def maxProfitII(self, prices: List[int]) -> int:
        # maxProfit=0
        # for i in range(len(prices)-1):
        #     if prices[i]<prices[i+1]:
        #         maxProfit+=prices[i+1]-prices[i]
        # return maxProfit
        dp = [0 for i in range(len(prices))]
        curr_max = 0 #record max profit upto i-th day
        temp = dp[0]-prices[0]
        for i in range(len(prices)):
            dp[i] = max(prices[i]+temp, curr_max)    
            temp = max(temp, dp[i]-prices[i])
            curr_max = max(curr_max, dp[i])
        return dp[-1]

obj = Solution()
prices = [7,6,4,3,1]
print(obj.maxProfitII(prices))