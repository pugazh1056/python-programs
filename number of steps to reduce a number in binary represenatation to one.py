class Solution:
    def numSteps(self, s: str) -> int:
        i = self.decimal(s)
        steps = 0

        while i != 1:
            if i % 2 == 0:
                i //= 2

            else:
                i += 1

            steps += 1


        return steps




    def decimal(self , s):
        return int(s , 2)
        
