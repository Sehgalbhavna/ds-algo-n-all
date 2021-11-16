'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = ""
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        while l1 >= 0 or l2 >= 0 or carry > 0:
            if l1 >= 0:
                carry += int(num1[l1])
                l1 -= 1
            if l2 >= 0:
                carry += int(num2[l2])
                l2 -= 1
            result += str(carry % 10)
            carry = carry // 10
            print(result)
        return result[::-1]
    
    def addStrings_ascii(self, num1: str, num2: str) -> str:
        r1 , r2 = 0, 0
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        for i in num1:
            r1 += (ord(i) - 48) * (10 ** l1)
            l1 -= 1
        for j in num2:
            r2 += (ord(j) - 48) * (10 ** l2)
            l2 -= 1
        return str( r1 + r2)
    
obj = Solution()
num1 = "456"
num2 = "77"
print(obj.addStrings_ascii(num1, num2))                