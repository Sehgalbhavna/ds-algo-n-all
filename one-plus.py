def plus_one(digit):
    # carry = 0
    # num = ""
    # for i in range(len(digit)):
    #     num += str(i)
    # num = int(num)
    # num += 1
    # arr = []
    # for i in str(num):
    #     arr.append(int(i))
    # return arr
    num = ""
    for i in digit:
        num +=str(i)
    num = int(num)
    num+=1
    num = str(num)
    ans = []
    for i in num:
        ans.append(int(i))
    return ans
        
digit = [1,9,9]

print(plus_one(digit))