class Solution:
    def trap(self, height: list[int]) -> int:
        
        if not height:
            return 0
        
        n = len(height)
        l = 0
        r = n - 1
        l_max = 0
        r_max = 0
        trapped_water = 0
        
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            
            if height[l] < height[r]:
                trapped_water += max(0, l_max - height[l])
                l += 1
            else:
                trapped_water += max(0, r_max - height[r])
                r -= 1
                
        return trapped_water