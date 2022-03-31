
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        last=chars[0]
        freq=1
        write=0 # where do we write in the chars array
        
		# loop till +1 to incorporate frequency of the last unique element
        for i in range(1,len(chars)+1):
                        
            if i<len(chars) and chars[i]==last:
                freq+=1
            
            if i==len(chars) or chars[i]!=last:
                chars[write]=last
                write+=1
                
                if freq>1: # O(1) -> # of digits in max frequency
                    #for n in str(freq):
                    chars[write]=str(freq)
                    write+=1
                
                if i<len(chars):
                    freq=1
                    last=chars[i]            
        
        return write

obj = Solution()
chars = ["a","a","b","b","c","c","c"]
print(obj.compress(chars))