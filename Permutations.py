class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start, used):
            if len(start) == len(nums):
                res.append(start[:])
                return True
         
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    start.append(nums[i])
                    backtrack(start, used)

                    start.pop()
                    used[i] = False
        backtrack([], [False] *len(nums))
        return res            
                    




        
