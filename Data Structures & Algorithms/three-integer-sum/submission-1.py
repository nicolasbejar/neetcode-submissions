class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_sorted = sorted(nums)


        ans = []
        for l in range(len(nums_sorted) - 2):
            if l > 0 and nums_sorted[l] == nums_sorted[l-1]:
                continue
            m, r = l + 1, len(nums_sorted) - 1
            while m < r:
                total = nums_sorted[l] + nums_sorted[m] + nums_sorted[r]
                if total == 0:
                    ans.append([nums_sorted[l], nums_sorted[m], nums_sorted[r]])
                    while m < r and nums_sorted[m] == nums_sorted[m+1]:
                        m += 1
                    while m < r and nums_sorted[r] == nums_sorted[r-1]:
                        r -= 1
                    m += 1
                    r -= 1
                elif total < 0:
                    m += 1
                else:
                    r -= 1

        return ans