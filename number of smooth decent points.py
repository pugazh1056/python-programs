class Solution(object):
    def getDescentPeriods(self, prices):
        """
        Count all descent periods by finding consecutive
        sequences where price decreases by exactly 1
        
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        result = 0
        i = 0
        
        while i < n:
            # Start of a descent sequence
            j = i
            
            # Extend while prices decrease by 1
            while j + 1 < n and prices[j] - prices[j+1] == 1:
                j += 1
            
            # Found a sequence from i to j
            length = j - i + 1
            result += length * (length + 1) // 2
            
            # Move to next sequence
            i = j + 1
            
        return result