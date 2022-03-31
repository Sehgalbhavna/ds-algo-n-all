from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        print(grid)
        m, n = len(grid), len(grid[0])

        print("-------------------------")
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        print(grid)
        print("-------------------------")
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        print(grid)
        print("-------------------------")

        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j -1])
        print(grid)
        return grid[m - 1][n - 1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
obj = Solution()

print(obj.minPathSum(grid))