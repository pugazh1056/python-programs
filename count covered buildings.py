class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        min_row = defaultdict(lambda: float('inf'))
        max_row = defaultdict(lambda: float('-inf'))
        min_col = defaultdict(lambda: float('inf'))
        max_col = defaultdict(lambda: float('-inf'))

        for r, c in buildings:
            if r < min_row[c]:
                min_row[c] = r
            if r > max_row[c]:
                max_row[c] = r
            if c < min_col[r]:
                min_col[r] = c
            if c > max_col[r]:
                max_col[r] = c

        count = 0
        
        for r, c in buildings:
            vertical_check = min_row[c] < r < max_row[c]
            horizontal_check = min_col[r] < c < max_col[r]
            if vertical_check and horizontal_check:
                count += 1
                
        return count