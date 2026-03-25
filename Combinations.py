class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, combination):
            if len(combination) == k:
                res.append(combination[:])
                return
            for nc in range(start,n+1):
                combination.append(nc)
                backtrack(nc+1,combination)
                combination.pop()

        ans = []
        backtrack(1, [])
        return res
