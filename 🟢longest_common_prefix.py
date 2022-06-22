strs = ["flower", "flow", "flight", "flying"]
# strs.sort(key=len)


def longestCommonPrefix(strs):
    result = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or strs[0][i] != s[i]:
                return result
        result += s[i]

    return result


print(longestCommonPrefix(strs))
