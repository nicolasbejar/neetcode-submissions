class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)        
        shortest = strs[0]
        longest = strs[len(strs)-1]
        ans = ""
        for i in range(len(shortest)):
            if shortest[i] == longest[i]:
                ans += shortest[i]
            else:
                return ans
        
        return ans
