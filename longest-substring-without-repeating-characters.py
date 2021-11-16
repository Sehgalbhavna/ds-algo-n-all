'''Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0 '''
# def lengthOfLongestSubstring(s):
#     str_set = set(s)
#     return len(str_set)

# def lenoflong(idx,s):
#     t_str=[]
#     i_dx = 0
#     for i in range(idx,len(s)):
#         i_dx += 1
#         if s[i] in t_str:
#             return i_dx-1 , t_str
#         else:
#             t_str.append(s[i])
#     return i_dx,t_str

# counter = 0
# num_lst=[]
# src='dvdf'
# if len(src):
#     while (counter < len(src)):
#         c,s = lenoflong(counter,src)
#         counter = counter + c
#         num_lst.append(len(s))
#         print(s)
#         #print(len(s))
#     print(max(num_lst))
#     #print((num_lst)) 
# else:
#     print(len(src))
   
    
    
#print (lenoflong(0,'pwwkew'))

# O(n*n)
def lengthOfLongestSubstring(s):
    newStr = ""
    lengthoglongest = 0
    for c in s:
        while c in newStr:
            newStr = newStr[1:]
        newStr += c
        if len(newStr) > lengthoglongest:
            lengthoglongest = len(newStr)
    return lengthoglongest
    
        
print(lengthOfLongestSubstring("abcabcdb"))    
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("dvdf"))

    