class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for charT in t:
            countT[charT] = 1 + countT.get(charT, 0)

        have, need = 0, len(countT)

        resultP, resultLength = [0, 0], float("infinity")
        l = 0

        for r in range(len(s)):
            charS = s[r]

            window[charS] = 1 + window.get(charS, 0)

            if charS in countT and countT[charS] == window[charS]:
                have += 1

            while have == need:
                if (r - l + 1) < resultLength:
                    resultP = [l, r]
                    resultLength = r - l + 1

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = resultP

        if resultLength != float("infinity"):
            return s[l : r + 1]
        else:
            return ""

