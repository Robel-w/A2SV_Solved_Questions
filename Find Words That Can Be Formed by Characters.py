class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = 0
        mapp = {}
        for ch in chars:
            if ch in mapp:
                mapp[ch] += 1
            else:
                mapp[ch] = 1
        for s in words:
            flag = True
            maap = mapp.copy()
            for i in s:
                if i in maap and maap[i] > 0:
                    maap[i] -= 1
                else:
                    flag = False
                    break    
            if flag:
                c += len(s)
                
        return c        
 

        
