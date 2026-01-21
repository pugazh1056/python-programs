class Solution:
    def minBitwiseArray(self,nums):
        res=[]
        for a in nums:
            b=a+1
            if a==2: # even prime, no answer
                res.append(-1)
            else:
                res.append(a-((b)&(-b))//2) # smallest number
        return res
