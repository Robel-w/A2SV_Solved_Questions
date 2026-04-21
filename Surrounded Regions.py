class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [(0,1), (0,-1), (1,0),(-1,0)]

        def dfs(row, col):
            if row<0 or row>= rows  or col <0 or col >= cols  or board[row][col] != 'O':
                return 
            board[row][col] = 'R'
            #for dr, dc in directions:
                #dfs(row+dr, col+dc)
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row, col-1)    
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        for i in range(cols):
            dfs(0, i)
            dfs(rows-1, i)    
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'R':
                    board[row][col] = 'O' 

                               
                

        
