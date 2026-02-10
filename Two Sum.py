class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in value_index:
                return [value_index[diff], i]
            value_index[num] = i
           