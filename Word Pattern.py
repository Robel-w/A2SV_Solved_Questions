class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        map1 = {}
        map2 = {}    


        for c, w in zip(pattern, words):
            if ((c in map1 and map1[c] != w) or (w in map2 and map2[w] != c)):
                return False
            map1[c] = w
            map2[w] = c
        return True        
        