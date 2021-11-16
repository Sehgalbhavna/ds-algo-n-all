def repeatedString(s, n):
    count = 0
    result = ''
    tem = 0
    for i in s:
        if i == 'a':
            count += 1 
    while len(s) < n:
        for i in s:
            if i == 'a':
               count += 1 
            s += i
            if len(s) == n:
                break
    return count
def repeatedString_2(s, n):
    cnt_a = 0
    str_postion = ''
    cnt_res = 0
    for i in range(len(s)):
        if s[i] == 'a':
            cnt_a = cnt_a + 1
            str_postion = str_postion + '1'
        else:
            str_postion = str_postion + '0'
    
    for i in range(n%len(s)):
        if str_postion[i] == "1":
            cnt_res = cnt_res + 1
    
    result = (n//len(s) ) * cnt_a + cnt_res
    
    print (cnt_a,str_postion,cnt_res,result)
        
def repeatedString_3(s,n):
    s, n = input().strip(), int(input().strip())
    print(s, n)
    result = s.count("a") * (n // len(s))
    result += s[:n % len(s)].count("a")
    print(result)

repeatedString_3('aba', 10)
#print(result)