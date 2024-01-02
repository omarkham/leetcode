class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        
        if len(nums) == 0:
            return []
        
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        result = []
        while True:
            row = []
            for num in counts:
                if counts[num] > 0:
                    row.append(num)
                    counts[num] -= 1
            
            if len(row) == 0:
                break
            result.append(row)
            
        return result