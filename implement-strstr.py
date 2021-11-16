class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if len(needle) == 0 or haystack == needle:
        #     return 0
        # if len(haystack) < len(needle):
        #     return -1
        # i=0
        # while i<len(haystack):
        #     if(needle==haystack[i:i+len(needle)]):
        #         return i
        #     else:
        #         i=i+1
        # return -1
        
        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack) - len(needle) +1 ):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


obj = Solution()
haystack = "aaaaa"
needle = ""
print(obj.strStr(haystack, needle))
            