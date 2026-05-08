class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indegre = [0 for _ in range(n)]
        q = deque()
        res = []
        for ansistor, c in edges:
            graph[ansistor].append(c)
            indegre[c] += 1

        c= [set() for _ in range(n)]
        q = deque([i for i in range(n) if indegre[i] == 0])   

        while q:
            cur = q.popleft()
            for par in graph[cur]:
                c[par].add(cur)
                c[par].update(c[cur])

                indegre[par] -= 1
                if indegre[par] == 0:
                    q.append(par)
        return [sorted(list(s)) for s in c]


            
        
