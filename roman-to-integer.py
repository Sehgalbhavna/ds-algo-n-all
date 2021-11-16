class Solution:
    def romanToInt(self, s: str) -> int:
        roman_sign = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        
        l = len(s)
        i = 0
        total = 0
        
        while i <= l -1:
            if i + 1 < len(s) and roman_sign[s[i]] < roman_sign[s[i + 1]]:
                total += roman_sign[s[i + 1]] - roman_sign[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += roman_sign[s[i]]       
            i += 1
        return total

obj = Solution()
print(obj.romanToInt('LVI'))