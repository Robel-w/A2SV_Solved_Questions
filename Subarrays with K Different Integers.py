class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            l = 0
            count = 0
            mp = {}
            for right in range(len(nums)):
                mp[nums[right]] = mp.get(nums[right], 0) + 1
                while len(mp) > k:
                    mp[nums[l]] -= 1
                    if mp[nums[l]] == 0:
                        del mp[nums[l]]
                    l += 1    
                
                count += (right - l+ 1)
            return count  
        return atMost(k) - atMost(k-1)              



        
