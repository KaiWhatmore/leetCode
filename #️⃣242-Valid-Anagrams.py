def isAnagram(s, t):
    checkAnagramS = {}
    checkAnagramT = {}

    if len(s) != len(t):
        return False

    for charS in s:
        checkAnagramS[charS] = checkAnagramS.get(charS, 0) + 1

    for charT in t:
        if charT not in checkAnagramS:
            return False
        checkAnagramT[charT] = checkAnagramT.get(charT, 0) + 1

    for valueS in checkAnagramS:
        if checkAnagramS[valueS] != checkAnagramT[valueS]:
            return False
    return True


print(isAnagram("cat", "tca"))
