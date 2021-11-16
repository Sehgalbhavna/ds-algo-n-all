class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            List_s = list(s)
            for i in t:
                if i not in List_s:
                    return False
                List_s.remove(i)
        return True
    
    def isAnagram2(self, s: str, t: str) -> bool:
        DS = {}
        DT = {}
        
        for i in s:
            if i in DS.keys():
                DS[i] += 1
            else:
                DS[i] = 1
        for i in t:
            if i in DT.keys():
                DT[i] += 1
            else:
                DT[i] = 1
        return DS == DT
                
    
    
obj1 = Solution()
s = "acc"
t = "cca"
print(obj1.isAnagram2(s,t))