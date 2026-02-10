class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = defaultdict(list)
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s in anagram:
                anagram[s].append(strs[i])
            else:
                anagram[s] = [strs[i]]
        res = []
        for value in anagram.values():
            res.append(value)
        return res        

        





        
