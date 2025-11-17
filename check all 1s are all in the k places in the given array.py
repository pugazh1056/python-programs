class Solution(object):
    def kLengthApart(self, nums, k):
        prev = -10**9
        for i, x in enumerate(nums):
            if x == 1:
                if i - prev <= k:
                    return False
                prev = i
        return True