from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        #self.quicksort(intervals,0,len(intervals)-1)
        stack = []
        stack.append(intervals[0])
        for current in intervals:
            previous = stack[-1]
            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
            else:
                stack.append(current)
        return stack

obj1 = Solution()
intervals = [[1,3],[8,10],[2,6],[15,18]]
result = obj1.merge(intervals)
print(result)
        