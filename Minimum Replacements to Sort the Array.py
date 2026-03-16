class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        maxx = nums[-1]
        res =0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > maxx:
                t = nums[i] // maxx
                if nums[i] % maxx:
                    t += 1
                maxx = nums[i]  // t
                res += t-1
            else:
                maxx = nums[i]
        return res            
                    
