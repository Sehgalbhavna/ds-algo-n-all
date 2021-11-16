class Solution:
    def reverse1(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        remain_x = abs(x)
        result = 0
        while remain_x > 0:
            remain_x, digit = divmod(remain_x,10)
            digit_bound = INT_MAX % 10 if x > 0 else INT_MAX % 10 + 1
            
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > digit_bound):
                return 0
            result = result * 10 + digit
        return result if x >= 0 else -result
    
    
    def reverse2(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        result = 0
        if x < INT_MIN or x > INT_MAX:
            return 0
        if x < 0:
            result = int("-" + str(-x)[::-1])
        else:
            result = int(str(x)[::-1])
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result

obj1 = Solution()

x = [123, -123, 120, 0,1534236469]
for i in x:
    print("***: ",i)
    print(obj1.reverse1(i))
    print(obj1.reverse2(i))
       