def characterReplacement(s, k):

    letterChecker = {}
    l = 0
    result = 0

    for r in range(len(s)):
        letterChecker[s[r]] = letterChecker.get(s[r], 0) + 1

        if (r - l + 1) - max(letterChecker.values()) > k:
            letterChecker[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)

    return result


print(characterReplacement("AABABBA", 1))
