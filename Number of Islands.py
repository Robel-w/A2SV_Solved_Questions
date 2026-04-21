class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        directions = [(0,1), (0,-1), (1,0),(-1,0)]

        def dfs(row, col):
            if row <0 or row >= rows or col <0 or col >= cols or grid[row][col] == '0':
                return 
            grid[row][col] ='0'
            for dr, dc in directions:
                dfs(row+dr, col+dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    island += 1
                    dfs(row, col)
        return island            

        
