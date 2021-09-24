from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        step1: iterate all the cells that allocate on the boarder of the board
        step2: if board[i][j] == 'O' dfs to find other O cells that are connected to this border cell,marked as "#"(will chage back to 'O' later)
        step3: iterate through non-boarder cells if  board[i][j] == 'O' change to 'X'
        
                 
        """
        m, n = len(board), len(board[0])
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    self.dfs(board, i, j)
        for j in [0, n - 1]:
            for i in range(m):
                if board[i][j] == 'O':
                    self.dfs(board, i, j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        
                
    def dfs(self, board, i, j):
        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
            return 
        board[i][j] = '#'
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)
        
           
            
        
            