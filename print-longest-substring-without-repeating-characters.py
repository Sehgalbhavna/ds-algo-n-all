def findLongestSubstring(s):
    n = len(s)
    st_point = 0
    current_len = 0
    maxlen = 0
    start = 0
    
    pos = {}
    pos[s[0]] = 0
    
    for i in range(1, n):
        if s[i] not in pos:
            pos[s[i]] = i
        else:
            if pos[s[i]] >= st_point:
                current_len = i - st_point
                maxlen = max(maxlen, current_len)
                start = st_point
                st_point = pos[s[i]] + 1
            pos[s[i]] = i
    maxlen = max(maxlen, i - st_point)
    start = st_point
    return s[start: start + maxlen]

print(findLongestSubstring("javaisgreat"))
    