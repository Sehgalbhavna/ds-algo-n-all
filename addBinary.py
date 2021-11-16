class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:sum += ord(a[i]) - ord('0')
            if j >= 0:sum += ord(b[j]) - ord('0')
            i , j = i - 1, j - 1
            carry = 1 if sum > 1 else 0
            result += str(sum % 2)
        if carry != 0:
            result += str(carry)
        return result[::-1]
        
        
    
    def addBinary2(self, a: str, b: str) -> str:
        indexA, indexB = len(a)-1, len(b)-1
        carry = 0
        res = ""

        while indexA >= 0 or indexB >= 0:
            if indexA >= 0:
                if a[indexA] == "1": carry += 1
                indexA -= 1
            if indexB >= 0:
                if b[indexB] == "1": carry += 1
                indexB -= 1    
            res = str(carry%2) + res
            carry //= 2
        
        if carry: res = "1" + res
        return res
a = "11"   
b = "1"    
Obj = Solution()
print(Obj.addBinary(a,b))
print(Obj.addBinary2(a,b))