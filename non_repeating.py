# Implement your function below.
def non_repeating(given_string):
    char_count = {}
    for i in given_string:
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] += 1
    for i in given_string:
        if char_count[i] == 1:
            return i
    return None
            
# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab")) # should return 'c'
print(non_repeating("abab")) # should return None
print(non_repeating("aabbbc")) # should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'