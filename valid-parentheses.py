class Solution:
    
    def isValid(self, s: str) -> bool:
        open_list = ["[","{","("]
        close_list = ["]","}","("]
        stack = []
        
        for i in s:

            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                print(open_list[pos])
                if (len(stack) > 0) and (open_list[pos] == stack[len(stack)-1]):
                    stack.pop()
                else:
                    return False
       
        if len(stack) == 0:
            return True
        else:
            return False
        
    def isValid2(self, s: str) -> bool:
        stack = []
        open_list = ["[","{","("]
        for i in s:
            if i in open_list:
                stack.append(i)
            else:
                if not stack: return False
                
                char = stack.pop()
                if i == "}":
                    if char != "{": return False
                if i == "]":
                    if char != "[": return False
                if i == ")":
                    if char != "(": return False
        return len(stack) == 0

s = "([])"
obj = Solution()
print(obj.isValid2(s))