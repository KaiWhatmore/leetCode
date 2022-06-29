def strStr(self, haystack: str, needle: str) -> int:
    # h 0
    # e 1
    # l 2, count ->1
    # l 3, count ->2
    # 0 4

    # heeell, ll

    if needle.strip() == "":
        return ""

    for i in range(haystack):
        if haystack[i : i + len(needle)] == needle:
            return i

    return -1
