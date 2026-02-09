class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        di = Counter(nums)
        for i, v in di.items():
            if v == 1:
                return i
