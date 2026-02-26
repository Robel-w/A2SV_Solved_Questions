class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        j = 0
        longest, maxx_count= 0, 0
        for i in range(len(s)):
            mp[s[i]] += 1
            maxx_count = max(maxx_count, mp[s[i]])
            while maxx_count +k < i-j+1:
                mp[s[j]] -=1
                j +=1
            longest = max(longest, i-j+1)    
        return longest

                
        
