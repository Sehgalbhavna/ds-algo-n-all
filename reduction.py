def reduction(num):
    sum = 0
    i = 0
    while len(num) != 1:
        sum = num[i] +num[i+1]
        num = num + [sum]
        print(num)
    print(num)
    
reduction([4,6,8])
         