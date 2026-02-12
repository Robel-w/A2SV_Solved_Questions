class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)
        for response in responses:
            for res in set(response):
                count[res] += 1
        maX = max(count.values())
        common = min([ k for k, v in count.items() if v == maX])        
        return common