class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mps = Counter(s)
        mpt = Counter(t)
        count = 0
        for key, value in mps.items():
            if key not in mpt:
                count += value
            elif value > mpt[key]:
                count +=(value - mpt[key])
        return count