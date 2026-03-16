class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        diff = []
        for c1, c2 in costs:
            diff.append([c2 - c1, c2, c1])
        diff.sort()
        for i in range(len(costs)):
            if i < len(costs) // 2:
                res += diff[i][1]  
            else:
                res += diff[i][2]
        return res             
