import collections
from collections import deque
class HitCounter:
    def __init__(self):
        self.d = deque()
        

    def hit(self, timestamp: int) -> None:
        self.d.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.d and timestamp - self.d[0] >= 300:
            self.d.popleft()
        return len(self.d)
        


# Your HitCounter object will be instantiated and called as such:
["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]

timestamps = [[],[1],[2],[3],[4],[300],[300],[301]]
obj = HitCounter()
for timestamp in timestamps:
    obj.hit(timestamp)
    param_2 = obj.getHits(timestamp)