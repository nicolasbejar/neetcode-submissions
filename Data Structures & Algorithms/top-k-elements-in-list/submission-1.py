class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency=Counter(nums)
    
        ans = sorted(frequency, key= frequency.get, reverse= True)[:k]
        return(ans)