class Solution:
    def minBitwiseArray(self, a: List[int]) -> List[int]:
        return [next((u for u in range(v) if u|-~u==v),-1) for v in a]
