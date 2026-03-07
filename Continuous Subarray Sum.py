class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:-1}
        pfx =0
        for i in range(len(nums)):
            pfx += nums[i]
            rem = pfx % k
            if rem in mp:
                if i - mp[rem] >=2:
                    return True
            else:    
                mp[rem] = i
        return False       
