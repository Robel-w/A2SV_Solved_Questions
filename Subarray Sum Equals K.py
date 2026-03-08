class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        pfx = 0
        cnt = 0
        rem =0
        for num in nums:
            pfx += num
            rem = pfx - k 
            if rem in mp:
                cnt += mp[rem]
            mp[pfx] = mp.get(pfx, 0) +1
        return cnt         
         

        
