class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n ==0:
            return 0 

        if n <= 2:
            return max(nums)
        
        dp1 = [0] * (n-1)
        dp2 = dp1.copy()

        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        # First One - from (0) to (N-1)
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1]) 

        # Second One - from (1) to N
        for j in range(2, n-1):
            dp2[j] = max(dp2[j-2] + nums[j+1], dp2[j-1])

        
        return max(dp1[-1], dp2[-1])
