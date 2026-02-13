class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        sorted_mp = sorted(mp.items(), key=lambda item: -item[1], )
        print(sorted_mp)
        i = 0
        res =[]
        for key, value in sorted_mp:
            if i < k:
                res.append(key)
                i += 1
        return res