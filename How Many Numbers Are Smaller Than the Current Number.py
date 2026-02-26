class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        count = {}
        for num, i in enumerate(sortedNums):
            if i not in count:
                count[i] = num
        return [count[i] for i in nums]   
     

        
