class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev = 0
        res = 0
        for i in reversed(s):
            curr = mp[i]
            if curr < prev:
                res -= curr
            else:
                res += curr
            prev = curr    

        return res   
