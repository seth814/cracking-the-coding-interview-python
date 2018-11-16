def is_substring(string, sub):
    return string.find(sub) != -1

def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False

result = string_rotation('waterbottle', 'erbottlewat')
print(result)
