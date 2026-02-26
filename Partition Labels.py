class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {c: i for i, c in enumerate(s)}

        res = []
        l = 0
        r = 0

        for i, c in enumerate(s):
            r = max(r, last_idx[c])

            if i == r:
                res.append(r - l + 1)
                l = r + 1
        return res
        
