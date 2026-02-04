class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        lis =[] 
        for i in range(left, right +1):
            lis.append(i)            
        
        for i in range(len(ranges)):
            s = ranges[i][0]  
            e = ranges[i][1]
            for j in range(s, e+1):
                if j in lis:
                    lis.remove(j)
                

        return len(lis) == 0            


                    


