class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = {}
        for i in magazine:
            res[i] = res.get(i, 0) + 1

        for i in ransomNote:
            if i not in res or res[i] == 0:
                return False
            res[i] -= 1
        return True           
        