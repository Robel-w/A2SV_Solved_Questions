class Solution:
    def frequencySort(self, s: str) -> str:
        mp = Counter(s)
        sorted_items = sorted(mp.items(), key=lambda x: x[1], reverse=True)
        result = []
        for char, freq in sorted_items:
            result.append(char * freq)
        
        return ''.join(result)
