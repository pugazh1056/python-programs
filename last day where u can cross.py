class Solution:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.cells = []
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def latestDayToCross(self, row, col, cells):
        self.row = row
        self.col = col
        self.cells = cells
        
        left = 1
        right = len(cells)
        while left < right:
            mid = right - (right - left) // 2
            if self.canCross(mid):
                left = mid
            else:
                right = mid - 1
        return left
    
    def canCross(self, day):
        grid = [[0] * self.col for _ in range(self.row)]
        for i in range(day):
            grid[self.cells[i][0] - 1][self.cells[i][1] - 1] = 1
        
        for i in range(self.col):
            if grid[0][i] == 0 and self.dfs(grid, 0, i):
                return True
        return False
    
    def dfs(self, grid, r, c):
        if r < 0 or r >= self.row or c < 0 or c >= self.col or grid[r][c] != 0:
            return False
        
        if r == self.row - 1:
            return True
        grid[r][c] = -1
        for direction in self.directions:
            i = r + direction[0]
            j = c + direction[1]
            if self.dfs(grid, i, j):
                return True
        return False
