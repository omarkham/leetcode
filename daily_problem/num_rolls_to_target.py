class Solution:
    def numRollsToTarget(self, n:int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        #1D array
        dp = [0] * (target + 1)
        #base case
        dp[0] = 1
        
        #dynamic programming
        for i in range(1, n + 1):
            
            new_dp = [0] * (target + 1)
            
            for j in range(1, target + 1):
                for face in range(1, k + 1):
                    if face <= j:
                        new_dp[i] = (new_dp[j] + dp[j - face]) % MOD
                    
                dp = new_dp
                
        return dp[target]