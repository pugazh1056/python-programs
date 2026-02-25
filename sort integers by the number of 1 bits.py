class Solution(object):
    def sortByBits(self, arr):
        count={}
        for num in arr:
            binary=bin(num)[2:]
            ones=binary.count("1")
            if ones not in count:
                count[ones]=[]
            count[ones].append(num)
        
        for k in count:
            count[k].sort()

        res=[]
        for i in sorted(count.keys()):
            res.extend(count[i])
        return res
