def strStr(haystack, needle):
    if needle == "":
        return 0

    for i in range(len(haystack)):
        if needle == haystack[i : i + len(needle)]:
            return i
    return -1


print(strStr("hello", "ll"))
