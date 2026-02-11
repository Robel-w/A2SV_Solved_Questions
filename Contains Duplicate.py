class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = Counter(nums)
        return True if len(mp) < len(nums) else False    
