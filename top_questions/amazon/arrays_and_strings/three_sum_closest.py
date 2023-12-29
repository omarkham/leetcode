class Solution:
    def threeSumClosest(self, nums: list[int]) -> list[list[int]]:
       
#better solution:

        nums.sort()
        return self.KSumClosest(nums, 3, target)
    
    def KSumClosest(self, nums: list[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])
        
        #target too small
        current = sum(nums[:k])
        if current >= target:
            return current
        
        #target too big
        current = sum(nums[-k:])
        if current <= target:
            return current
        
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]
        
        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i > 0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current
                    
        return closest
            
#original solution (works, just slower)            
'''
        nums.sort()
        closest_sum = float("inf")
        
        #since we want at least 2 numbers to the right of current number
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                #update closest_sum if the current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                     closest_sum = current_sum
                     
                #since we sorted it
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return closest_sum
                
        return closest_sum
'''