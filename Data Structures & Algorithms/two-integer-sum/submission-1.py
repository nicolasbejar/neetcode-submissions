class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        aux = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in aux:
                return [aux[diff], i]
            else:
                aux[n] = i