def comapair_string_as_number(str1, str2):
    flag =False
    if len(str1) > len(str2):
        return True
    elif len(str1) < len(str2):
        return False
    elif len(str1) == len(str2):
        for i in str1:
            for j in str2:
                if i < j:
                    flag = False
                elif i == j:
                    flag = False    
                else:
                    flag = True
        return flag

def comapair_string_as_number2(str1, str2):
    flag =False
    if len(str1) > len(str2):
        return True
    elif len(str1) < len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            continue
        elif str1[i] > str2[i]:
            return True
        else: #str1[i] < str2[i]:
            return False
    return False

#Test1    
str1 = "113"
str2 = "112"
print(comapair_string_as_number(str1,str2))
print(comapair_string_as_number2(str1, str2))

#Test2    
str3 = "525"
str4 = "1111"
print(comapair_string_as_number(str3,str4))
print(comapair_string_as_number2(str3, str4))

#Test3    
str5 = "11"
str6 = "0"
print(comapair_string_as_number(str5,str6))
print(comapair_string_as_number2(str5, str6))

#Test4    
str7 = "1"
str8 = "1"
print(comapair_string_as_number(str7,str8))
print(comapair_string_as_number2(str7, str8))
            