class Solution(object):
    def countTrapezoids(self, points):
        """
        Count valid trapezoids formed by points where trapezoids have
        horizontal parallel bases (same y-coordinates)
        
        :type points: List[List[int]]
        :rtype: int
        """
        M = 10**9 + 7           # modulo for large results
        y_count = {}            # stores count of points at each y-level
        
        # 📊 GROUP POINTS: Count points at each y-coordinate
        for x, y in points:
            if y in y_count:
                y_count[y] += 1
            else:
                y_count[y] = 1
        
        counts = list(y_count.values())  # extract counts per level
        r = 0                            # total trapezoid count
        s = 0                            # cumulative pairs from previous levels
        
        # 🔄 PROCESS EACH LEVEL: Build trapezoids layer by layer
        for c in counts:
            if c >= 2:
                # 💡 COMBINATION MATH: pairs at current level
                w = c * (c - 1) // 2
                
                # 🎯 COUNT TRAPEZOIDS: current pairs × previous pairs
                r += w * s
                
                # 📈 UPDATE CUMULATIVE: add current pairs for future levels
                s += w
        
        return r % M