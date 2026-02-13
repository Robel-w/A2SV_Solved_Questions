class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        mp, left = {}, {}
        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        
        for i in range(len(nums) - 1):
            left[nums[i]] = left.get(nums[i], 0) + 1
            mp[nums[i]] -= 1

            if left[nums[i]] * 2 > (i + 1) and mp[nums[i]] * 2 > (len(nums) - i - 1):
                return i
        return -1          




