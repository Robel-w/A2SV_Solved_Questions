class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = Counter(nums)
        n = len(nums)
        s = []
        for k, v in mp.items():
            if v > n/ 3:
                s.append(k)
        return s 
