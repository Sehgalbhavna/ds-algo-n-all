from typing import List
from logging import exception
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = list()
        try:
            for i in range(1,n+1):
                if i % 15 == 0: result.append("FizzBuzz")
                elif i % 3 == 0: result.append("Fizz")
                elif i % 5 == 0: result.append("Buzz")
                else: result.append(str(i))
            return result
        except exception as e:
            print(str(e))

obj = Solution()
print(obj.fizzBuzz(16))