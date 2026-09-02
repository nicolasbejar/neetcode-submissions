from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        counterT = Counter(t)
        required = len(counterT)   # number of distinct chars in t we need to satisfy

        window = {}
        formed = 0                 # number of distinct chars currently satisfied
        l = 0
        shortest = ""

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in counterT and window[c] == counterT[c]:
                formed += 1

            # window is valid — try to shrink it from the left
            while formed == required:
                if shortest == "" or (r - l + 1) < len(shortest):
                    shortest = s[l:r+1]

                left_char = s[l]
                window[left_char] -= 1
                if left_char in counterT and window[left_char] < counterT[left_char]:
                    formed -= 1
                l += 1

        return shortest