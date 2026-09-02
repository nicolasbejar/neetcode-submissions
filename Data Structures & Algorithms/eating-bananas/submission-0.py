import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1 , max(piles)
        k = r 

        while l <= r:
            mid = l + (r - l) // 2
            time = 0
            for i in piles:
                time += math.ceil(i / mid)
            
            if time <= h: 
                k = mid
                r = mid -1
            else:
                l = mid +1
        
        return k
            


        