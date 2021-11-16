class Solution:
    def isPalindromeStr(self, x: int) -> bool:
        s = str(x)
        res = ""
        for i in range(len(s)-1, -1,-1):
            if s[i].isdigit():
                res += s[i]
            elif s[i] == '-':
                return False
        if int(res) == x:
            return True
        else:
            return False
        
    def isPalindrome(self, x: int) -> bool:    
        reverse = 0
        tmp = x
        if x == 0:
            return True
        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10
        return tmp == reverse

obj = Solution()
x = 596516506
print(x)
print(obj.isPalindrome(x))