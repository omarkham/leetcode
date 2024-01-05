class Solution:
    def minOperations(self, nums: list[int]) -> int:
        mp = Counter(nums)
        result = 0
        
        for v in mp.values():
            if v == 1: return -1
            result += math.ceil(v/3)
        
        return result