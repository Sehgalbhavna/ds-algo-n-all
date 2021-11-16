class Solution:
    def canConvert(self, str1, str2):
        dict = {}
        
        n = len(str1)

        if str1 == str2: return True
        
        for i in range(n):
            start, end = str1[i], str2[i]
            if start in dict and dict[start] != end:
                return False
            if start not in dict:
                dict[start] = end

        if len(dict.keys()) == 26 and len(list(set(dict.values()))) == 26:
            return False
            
        return True
    
str1 = "aabcc"
str2 = "ccdee"
obj = Solution()

print(obj.canConvert(str1,str2))