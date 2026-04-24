class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        def dfs(node, col):
            color[node] = col
            for negb in graph[node]:
                if color[negb] == col:
                    return False
                if color[negb] == 0 and not dfs(negb, -col):
                    return False
            return True
        
        for i in range(len(graph)):
            if color[i] == 0 and not dfs(i, 1):
                return False
                
        return True




        
