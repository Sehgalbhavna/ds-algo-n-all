from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        maxprefixlen = float('inf') 
        
        for i in strs:
            maxprefixlen=min(maxprefixlen,len(i))
        
        result = ""
        for i in range(maxprefixlen):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return result
            result += strs[0][i]
        return result
    
    def longestCommonPrefix_2(self, strs):
        if len(strs) == 0:
            return ""
        current = strs[0]
        for i in range(1,len(strs)):
            temp = ""
            if len(current) == 0:
                break
            for j in range(len(strs[i])):
                if j<len(current) and current[j] == strs[i][j]:
                    temp+=current[j]
                else:
                    break
            current = temp
        return current

obj = Solution()
# Test case 1    
strs = ["flower","flow","flight"]
print(strs)
print(obj.longestCommonPrefix(strs))
print(obj.longestCommonPrefix_2(strs))

# Test case 2   
strs2 = ["dog","racecar","car"]
print(strs2)
print(obj.longestCommonPrefix(strs2))
print(obj.longestCommonPrefix_2(strs2))

# Test case 3    
strs3 = []
print(strs3)
print(obj.longestCommonPrefix(strs3))
print(obj.longestCommonPrefix_2(strs3))

# Test case 4    
strs4 = ["",""]
print(strs4)
print(obj.longestCommonPrefix(strs4))
print(obj.longestCommonPrefix_2(strs4))

# Test case 5    
strs5 = ["aabc",""]
print(strs5)
print(obj.longestCommonPrefix(strs5))
print(obj.longestCommonPrefix_2(strs5))



            