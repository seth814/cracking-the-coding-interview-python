def unique(string):

    if len(string) > 128:
        return False

    chars = [False for _ in range(128)]
    for c in string:
        val = ord(c)
        if chars[val] == True:
            return False
        chars[val] = True

    return True

string = 'abcdef'
print(unique(string))
string = '%abcdef%'
print(unique(string))
