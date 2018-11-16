def one_away(s1, s2):
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    editted = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if editted:
                return False
            editted = True
    return True

def one_edit_insert(s1, s2):
    editted = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if editted:
                return False
            editted = True
            j += 1
        else:
            i += 1
            j += 1
    return True

print(one_away('pale', 'ple'))
print(one_away('pales', 'pale'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'ble'))
