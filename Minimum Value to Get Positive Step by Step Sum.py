class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pfx = 0
        minn = float('inf')
        for num in nums:
            pfx += num
            minn = min(minn, pfx)
        if minn > 0:
            return 1
        else:
            return 1 - minn        

        
