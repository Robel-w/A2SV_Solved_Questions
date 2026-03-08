class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pfx = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pfx
            pfx *= nums[i]
        sfx = 1    
        for i in range(len(nums)-1, -1,-1):
            res[i] *= sfx
            sfx *= nums[i]  
        return res        
        
