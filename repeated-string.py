def repeatedString(s, n):
    count = 0
    l = len(s)
    if len(s) == n:
        for i in n:
            if s[i] == 'a':
                count += 1
        return count
    else:
        while l != n:
            for i in range