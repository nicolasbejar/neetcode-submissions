from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        counters = Counter(nums)

        for i in counters:
            if counters[i] > 1:
                return i
        