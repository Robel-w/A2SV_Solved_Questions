class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        res = ''
        for char in order:
            res += char * cnt[char]
        for char in s:
            if char not in order:
                res += char    
        return res            
            
        
