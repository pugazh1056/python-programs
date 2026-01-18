class Solution:
    def largestMagicSquare(self, grid):
        R, C = len(grid), len(grid[0])

        row = [[0] * (C + 1) for _ in range(R)]
        col = [[0] * C for _ in range(R + 1)]

        for i in range(R):
            for j in range(C):
                row[i][j + 1] = row[i][j] + grid[i][j]

        for j in range(C):
            for i in range(R):
                col[i + 1][j] = col[i][j] + grid[i][j]

        ans = 1

        for i in range(R):
            for j in range(C):
                for size in range(min(R - i, C - j), ans, -1):
                    if self.isMagic(grid, row, col, i, j, size):
                        ans = size
                        break
        return ans

    def isMagic(self, g, r, c, x, y, l):
        target = r[x][y + l] - r[x][y]

        for i in range(l):
            if r[x + i][y + l] - r[x + i][y] != target:
                return False

        for j in range(l):
            if c[x + l][y + j] - c[x][y + j] != target:
                return False

        d1 = d2 = 0
        for k in range(l):
            d1 += g[x + k][y + k]
            d2 += g[x + l - 1 - k][y + k]

        return d1 == target and d2 == target
