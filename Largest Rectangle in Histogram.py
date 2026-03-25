class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        hts = heights + [0] 
        for i, h in enumerate(hts):
            while stack and hts[stack[-1]] > h:
                height = hts[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                res = max(res, height * w)
            stack.append(i)
        return res
