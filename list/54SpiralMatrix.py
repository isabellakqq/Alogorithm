from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m, n = len(matrix), len(matrix[0])
        # i = j = 0
        # res = []
        # i = 0
        # for j in range(n):
        #     res.append(matrix[0][j])
        # j = n -1
        # for i in range(1, m):
        #     res,append(matrix[i[n-1]])
        # i = m - 1
        # for j in range(1, n -1):
        #     res.append(matrix[m-1][j])
        #four directions:0:left -> right 1:top -> down  2:right -> left  3: down -> top
        #time:O(m*n) psace o(1)
        left, right = 0, len(matrix[0]) - 1
        top, down = 0, len(matrix) - 1
        res = []
        d = 0
        while left <= right and top <= down:
            if d == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
            elif d == 1:
                for i in range(top, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            elif d == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            elif d ==3:
                for i in range(down, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            d = (d + 1) % 4
        return res
    
                
                
        