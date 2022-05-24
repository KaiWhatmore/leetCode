class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCaseS = s.lower()
        newStr = ""
        result = True
        for str in lowerCaseS:
            if self.isAlphaNum(str):
                newStr += str
        if newStr.strip() == "" or len(newStr) == 1: 
            return True 

        l, r = 0, len(newStr) -1

        while l <= len(newStr) // 2:
            if newStr[l] != newStr[r]:
                result = False
            l += 1
            r -= 1

        return result


    def isAlphaNum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
        