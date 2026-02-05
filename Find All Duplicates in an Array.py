class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mapp ={}
        res = []
        for num in nums:
            mapp[num] = mapp.get(num, 0) + 1
        res = [k for k, v in mapp.items()  if v == 2] 
        return res          
    
