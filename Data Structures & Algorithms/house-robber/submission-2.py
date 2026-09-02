class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        if len(nums) <=2:
            return max(nums)

        dp = [0] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i]+ dp[i-2], dp[i-1])

        
        return dp[len(nums)-1]


        