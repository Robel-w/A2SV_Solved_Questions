class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        res = []
        def dfs(node):
            if len(graph) - 1 == node:
                res.append(path.copy())
                return 
            for negb in graph[node]:
                path.append(negb)
                dfs(negb)
                path.pop()
        dfs(0)
        return res             
