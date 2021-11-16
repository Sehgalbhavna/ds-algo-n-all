class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        maxprefixlen=float('inf') 
        for i in strs:
            maxprefixlen=min(maxprefixlen,len(i))
		
        result = ""
        for i in range(maxprefixlen):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[k][i]:
                    return result
                result += strs[0][i]
        return result
strs = ["flower","flow","flight"]
obj = Solution()

print(obj.longestCommonPrefix(strs))

            