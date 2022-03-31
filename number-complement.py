class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        else:
            b_num = self.decimalToBinary(num)
            c_num = ''
            for c in b_num:
                if int(c) == 0:
                    c_num += "1"
                else:
                    c_num += "0"
            d_num = self.binaryToDecimal(c_num)
            return d_num

    def decimalToBinary(self, num):
        if num == 0:
            return ''
        else:
            return self.decimalToBinary(num // 2) + str(num % 2)
    
    def binaryToDecimal(self, b_num):
        d_num = 0
        for n in b_num:
            d_num = d_num*2 + int(n)
        return d_num
            
        
    
obj = Solution()
print(obj.findComplement(0))
