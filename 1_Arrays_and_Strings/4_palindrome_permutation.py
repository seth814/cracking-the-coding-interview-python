def pal_perm(phrase):
    phrase = phrase.lower()
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    count_odd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                count_odd += 1
            else:
                count_odd -= 1
    return count_odd <= 1


def char_number(c):
    a = ord('a')
    z = ord('z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    return -1

result = pal_perm('Tact Coa')
print(result)
result = pal_perm('Not a palindrome')
print(result)
