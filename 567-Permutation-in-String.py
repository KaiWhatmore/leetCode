s1 = "ab"
s2 = "eidbaooo"


def checkInclusion(s1, s2):

    if len(s1) > len(s2):
        return False

    checkerS1 = {}

    for letterS1 in s1:
        checkerS1[letterS1] = 1 + checkerS1.get(letterS1, 0)

    for i in range(0, len(s2), len(s1)):
        checkerS2 = {}
        for j in range(len(s1)):
            checkerS2[s1[j]] = 1 + checkerS2.get(s1[j], 0)
        if checkerS1 == checkerS2:
            return True

    return False


print(checkInclusion(s1, s2))
