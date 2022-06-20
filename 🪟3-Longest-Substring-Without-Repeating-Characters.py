class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStringChecker = set()
        maxLength = 0
        l = 0

        for r in range(len(s)):
            while s[r] in subStringChecker:
                subStringChecker.remove(s[l])
                l += 1
            subStringChecker.add(s[r])
            maxLength = max(maxLength, len(subStringChecker))

        return maxLength
