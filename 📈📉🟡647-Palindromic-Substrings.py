def countSubstrings(s):
    result = 0

    for i in range(len(s)):

        # odd cases:
        l, r = i, i
        while l >= 0 and r < len(s) and s[r] == s[l]:
            result += 1
            l -= 1
            r += 1

        # even cases:
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[r] == s[l]:
            result += 1
            l -= 1
            r += 1

    return result


print(countSubstrings("aaab"))
