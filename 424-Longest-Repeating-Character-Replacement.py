# logic:
# if length(subString) - mostCommonLetter <= k
# then rightPointer += 1
# else leftPointer +=1
# rightPointer cannnot exceed bound of s
# keep track of max val of len(subString)
# # dictionary grows as subString increases


def characterReplacement(s, k):
    letterChecker = {}
    result = 0
    leftPointer = 0

    for rightPointer in range(len(s)):
        letterChecker[s[rightPointer]] = 1 + letterChecker.get(s[rightPointer], 0)

        if (rightPointer - leftPointer + 1) - max(letterChecker.values()) > k:
            letterChecker[s[leftPointer]] -= 1
            leftPointer += 1

        result = max(result, rightPointer - leftPointer + 1)

    return result


s = "ABAB"
k = 2

print(characterReplacement(s, k))
