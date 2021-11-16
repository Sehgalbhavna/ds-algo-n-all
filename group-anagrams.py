from typing import List
class Solution:  
    
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
        print(DS == DT)
        return DS == DT
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = []
        list2 = []
        for i in range(len(strs)):
            list1.append(strs[i])
            for j in range(i+1, len(strs)):
                result = self.isAnagram2(strs[i], strs[j])
                if result == True:
                    list1.append(strs[j])
                j += 1
            list2.append(list1)
            i += 1
        return list2
    
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword not in dict:
                dict[sortedword] = [word]
            else:
                dict[sortedword].append(word)
        result = []
        for item in dict.values():
            result.append(item)
        return result    
strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
print(obj.groupAnagrams2(strs))
                
            
    