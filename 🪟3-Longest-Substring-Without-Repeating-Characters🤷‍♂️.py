class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStringChecker = []
        leftP = 0
        result = 0

        for rightP in range(len(s)):
            while s[rightP] in subStringChecker:
                subStringChecker.remove(s[leftP])
                leftP += 1
            subStringChecker.append(s[rightP])
            result = max(result, rightP - leftP + 1)

        return result
