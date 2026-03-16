class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = res = 0
        maxx = deque()
        minn = deque()
        for r in range(len(nums)):
            while maxx and maxx[-1] < nums[r]:
                maxx.pop()
            while minn and minn[-1] > nums[r]:
                minn.pop()
            maxx.append(nums[r])
            minn.append(nums[r])

            while maxx[0] - minn[0] > limit:
                if maxx[0] == nums[l]:
                    maxx.popleft()
                if minn[0] == nums[l]:
                    minn.popleft()
                l += 1
            res = max(res, r-l+1)                     
    
        return res
        
