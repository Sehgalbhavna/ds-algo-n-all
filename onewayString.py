# Implement your function below.
def one_away_same_length(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count > 1:
                return False 
    return True

def one_away_diff_length(s1, s2):
    i = 0
    count = 0
    while i < len(s2):
        if s1[i + count] == s2[i]:
            i += 1
        else:
            count += 1
            if count > 1:
                return False
    return True

def is_one_away(s1, s2):
    if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
        return False
    elif len(s1) == len(s2):
        return one_away_same_length(s1, s2)
    elif len(s1) > len(s2):
        return one_away_diff_length(s1, s2)
    else:
        return one_away_diff_length(s2, s1)



# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "abc"))  # should return False
print(is_one_away("abcdef", "abcde"))  # should return True
