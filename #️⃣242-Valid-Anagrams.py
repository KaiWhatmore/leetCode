class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkAnagramS = {}
        checkAnagramT = {}

        if len(s) != len(t):
            return False

        for letterS in s:
            if letterS not in checkAnagramS:
                checkAnagramS[letterS] = 1
            else:
                checkAnagramS[letterS] += 1

        for letterT in t:
            if letterT not in checkAnagramT:
                checkAnagramT[letterT] = 1
            else:
                checkAnagramT[letterT] += 1

        for valueS in checkAnagramS.keys():
            if valueS not in checkAnagramT.keys():
                return False

        for valueS in checkAnagramS:
            if checkAnagramS[valueS] != checkAnagramT[valueS]:
                return False
        return True
