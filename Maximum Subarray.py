class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pfx = nums[0]
        maxx = nums[0]

        for i in range(1, len(nums)):
            pfx = max(nums[i], pfx + nums[i])
            maxx = max(maxx, pfx)

        return maxx
