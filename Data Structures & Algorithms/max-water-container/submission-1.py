class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        maxAreaAns = 0 

        l, r = 0, len(heights) -1

        while l < r: 
            distance = r - l 
            smallest = min(heights[l], heights[r])
            area = smallest * distance
            if area > maxAreaAns:
                maxAreaAns = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        
        return maxAreaAns
            
