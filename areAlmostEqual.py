class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count_diff = 0
        for i in range(len(s1)):
            if s1[i] not in s2 or s2[i] not in s1 :
                count_diff += 1
                if count_diff > 1:
                    return False
        return True
obj1 = Solution()
s1 = "abcd"
s2 = "dcba"
print(obj1.areAlmostEqual(s1, s2))