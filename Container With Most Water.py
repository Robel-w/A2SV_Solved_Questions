class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxx = float('-inf')
        high = 0
        while l < r:
            if height[l] < height[r]:
                high = height[l] * (r-l)
                l+=1
            elif height[l] > height[r]:  
                high = height[r] * (r-l)
                r -= 1
            else:
                high = height[l] * (r-l)
                r -=1
                l += 1

            maxx = max(high, maxx)
        return maxx    
    
