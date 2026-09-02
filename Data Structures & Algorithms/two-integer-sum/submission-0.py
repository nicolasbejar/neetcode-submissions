class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = {}

        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in ans:
                return [ans[compliment], i]            
            ans[n] = i