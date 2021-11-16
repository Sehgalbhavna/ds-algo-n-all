class Solution:
    cache = {}
    def numSquares1(self, n: int) -> int:
        cache = {}
        def dfs(n):
            if n in cache:
                return cache[n]
            if n == 0:
                return 0
            
            i = 1
            res = float("inf")
            
            while (i * i <= n):
                res = min(res,dfs(n - (i * i)))
                i += 1
            if n not in cache:
                cache[n] = 1 + res
            return cache[n]
        return dfs(n)
    
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        # bottom case
        dp[0] = 0
        
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], dp[target - square] + 1)
                #print(dp[target] )
        
        return dp[-1]
    
obj1 = Solution()
print(obj1.numSquares(13))