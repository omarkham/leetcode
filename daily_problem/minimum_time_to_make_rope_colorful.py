class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        if len(colors) < 2:
            return 0
        
        sum_cost, left, right = 0
        
        while right < len(neededTime) and left < len(neededTime):
            
            curTotal = 0
            curMax = 0
            
            while right < len(neededTime) and colors[left] == colors[right]:
                curTotal += neededTime[right]
                curMax = max(curMax, neededTime[right])
                right += 1
                
            sum_cost += curTotal - curMax
            left = right
            
        return sum_cost