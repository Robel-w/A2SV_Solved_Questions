class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pfx = 0
        diff = cnt =  0
        mp = {0:1}
        for i in range(len(nums)):
            pfx += nums[i]
            diff = pfx - goal
            cnt += mp.get(diff, 0) 
            mp[pfx] = mp.get(pfx, 0) + 1
        return cnt    
