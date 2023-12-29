class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        triplets = []
        
        #len(nums) - 2 so that we have at least two elements to the right of the current number
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplets.append(triplet)
                    
                    #to avoid duplicate triple results
                    while left < right and nums[left] == triplet[1]:
                        left += 1
                    while left < right and nums[left] == triplet[2]:
                        right -= 1
                #since we sorted it at the beginning
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return triplets