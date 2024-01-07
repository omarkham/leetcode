from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        total_count = 0
        
        #dp[i][diff] represents the number of arithmetic subsequences ending at index 'i' with the common difference 'diff'
        dp = [defaultdict(int) for _ in range(n)] #dp is a list of dictionaries (initialized with default values of 0)
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                
                if diff in dp[j]:
                    #accumulate the count of subsequences with the same difference ending at index j
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]
                    
        return total_count
        
        