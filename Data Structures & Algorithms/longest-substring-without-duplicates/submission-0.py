class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0
        current = ""
        maxLen = 0

        while r < len(s):

            while s[r] in current:
                current = current[1:]
                l += 1

            current += s[r]
            maxLen = max(maxLen, len(current))
            r += 1

        return maxLen