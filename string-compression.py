class Solution:
    def compress(self, chars):
        s = chars[0]
        count = 1
        for i in range(1,len(chars)):
            curr = chars[i]
            prev = chars[i -1]
            if curr == prev:
                count += 1
            else:
                if count > 1:
                    s += str(count)
                    count = 1
                s += curr
        if count > 1:
            s += str(count)
            count = 0
        return len(s)


    def compress2(self, chars):
        word_ct = 1
        start_pos = 0
            
        for ind, val in enumerate(chars):
            print(ind, val)
            #Last letter of the list or last letter of the group
            if ind + 1 == len(chars) or val != chars[ind+1]:
                
                #replace the letter in chars
                chars[start_pos] = val
                print(chars[start_pos])    
                #track the position
                start_pos += 1
                    
                if word_ct > 1:
                    for c in str(word_ct):
                        chars[start_pos] = c
                        start_pos += 1
                        print(chars[start_pos])
                        
                    
                #reset the word ct for the new group
                word_ct = 1
                
                
            else:
                word_ct += 1
        print(chars)            
        return start_pos 
ch1 = Solution()
result = ch1.compress2(["a","a","b","b","c"])
print(result)