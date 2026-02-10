class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mp = {}
        res = [0]*len(s)
        for i, ch in enumerate(s):
            res[indices[i]] = ch
        return "".join(res )