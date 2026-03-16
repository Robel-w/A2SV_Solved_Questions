class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * n
        res = 0

        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1

        for i in range(1,n):
            freq[i] += freq[i-1]
        nums.sort()
        freq.sort()

        for i in range(n):
            res = (res + (freq[i] * nums[i])) % (10**9 + 7)        
        return res
        
