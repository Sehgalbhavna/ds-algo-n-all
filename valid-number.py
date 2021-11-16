class Solution:
    def isNumber(self, s: str) -> bool:
        l = len(s)
        seenDigit, seen, seenDot = False, False, False
        countSign = 0
        
        for i in range(l):
            if s[i].isdigit():
                seenDigit = True
            
            elif s[i] == '+' or s[i] == '-':
                if countSign == 2: return False
                if i == l-1: return False
                if i > 0 and not (s[i-1] == 'e' or s[i-1] == 'E'):return False
                countSign += 1
            
            elif s[i] == '.':
                if seenDot == True: return False
                if seen == True: return False
                if i == l -1 and seenDigit == False: return False
                seenDot = True
            
            elif s[i] == 'e' or s[i] == 'E':
                if seen == True: return False
                if seenDigit == False: return False
                if i == 0 or i == l -1: return False
                seen = True
            else:
                return False
        return True
            
            
obj = Solution()
print(obj.isNumber('99e2.5'))