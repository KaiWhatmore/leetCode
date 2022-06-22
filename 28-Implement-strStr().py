def strStr(self, haystack: str, needle: str) -> int:
    # h 0
    # e 1
    # l 2, count ->1
    # l 3, count ->2
    # 0 4

    # heeell, ll

    if needle.strip() == "":
        return ""

    needleCheck = list(needle)
    count = 0
    for i, char in enumerate(haystack):
        if char in needleCheck:
            count += 1
            needleCheck.remove(char)

        if len(needleCheck) == 0:
            return len(haystack) - count - 1

    return -1
