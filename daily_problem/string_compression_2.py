class Solution:
    def getLengthOfOptimalCompression(self, s:str, k:int) -> int:
        
        n = len(s)
        #dp[i][j] = minimum length after processing the first i characters with j deletions
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        
        def encode_length(count):
            if count == 1:
                return 1
            return len(str(count))
       
        #iterate over each character and number of deletions 
        for i in range(n + 1):
            for j in range(k + 1):
                
                #base cases
                if j == 0 or i == 0:
                    dp[i][j] = 0
                    
                else:
                    
                    #case 1: delete the current character
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                    
                    #case 2: keep the current character
                    count = 0
                    l = i
                    while l > 0 and s[l - 1] == s[i - 1]:
                        l -= 1
                        count += 1
                        
                    length = encode_length(count)
                    
                    #update dp[i][j] with the minimum length after considering the current character
                    dp[i][j] = min(dp[i][j], dp[l][j - count] + length)
                    #move to the next character
                    dp[i][j] = min(dp[i][j], dp[l][j] + length)
                    
                    