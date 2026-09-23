from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counters = Counter(nums)

        return max(counters, key=counters.get)


        