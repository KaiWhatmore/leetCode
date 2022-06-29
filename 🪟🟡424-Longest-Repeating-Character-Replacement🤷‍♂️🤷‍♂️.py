# logic:
# if length(subString) - mostCommonLetter <= k
# then r += 1
# else l +=1
# r cannnot exceed bound of s
# keep track of max val of len(subString)
# # dictionary grows as subString increases


def characterReplacement(s, k):
    letterChecker = {}
    result = 0
    l = 0

    for r in range(len(s)):
        letterChecker[s[r]] = 1 + letterChecker.get(s[r], 0)

        if (r - l + 1) - max(letterChecker.values()) > k:
            letterChecker[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)

    return result


s = "ABAB"
k = 2

print(characterReplacement(s, k))
