class Solution:
    def myAtoi1(self, s: str) -> int:
        numbers = ["1","2","3","4","5","6","7","8","9","0","-","+"]
        result = ""
        sign = "-"
        if len(s) == 0:
            return None
        
        for i in s:
            if i == "0" and len(result) == 0:
                continue
            elif i in numbers:
                result += i
        
        return int(result)
    
    
    
    
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31    #-2147483648
        
        i = 0
        res = 0
        negative = 1
        
        #whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i < len(s) and s[i] == '-':
            i += 1
            negative = -1
        elif i < len(s) and s[i] == '+':
            i += 1    
            
        checker = set('0123456789')
        while i < len(s) and s[i] in checker:
            res = res * 10  + int(s[i])
            i += 1
        
        res = res * negative
        if res > MAX_INT :
            return MAX_INT 
        elif res < MIN_INT:
            return MIN_INT
        #check the MAX / MIN int
        return res 
            
obj = Solution()
print(obj.myAtoi("2147483648"))