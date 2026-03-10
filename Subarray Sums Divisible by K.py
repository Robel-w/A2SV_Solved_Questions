class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pfx =0
        mp = {0: 1}
        count = 0
        for i in range(len(nums)):
            pfx += nums[i]
            div = pfx % k
            if div in mp:
                count +=mp[div]
            mp[div] = mp.get(div, 0)+1
            print(mp)
        return count        

        
