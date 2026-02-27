class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        c = len(piles)//3
        summ = 0
        for i in range(1, len(piles) - c, 2):
            summ += piles[i]
        return summ




        
