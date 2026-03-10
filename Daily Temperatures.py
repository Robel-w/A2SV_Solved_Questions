class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono = [] 
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            while mono and mono[-1][0] <  temperatures[i]:
                val, ind = mono.pop()
                res[ind] = (i - ind)  
            mono.append([temperatures[i],i])    
    
        return res    


        
