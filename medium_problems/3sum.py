from typing import List

class Solution:
    #len(nums) - 2 so that we have at least two elements to the right of the current number
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for i in range(len(nums) - 2):
            #duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplets.append(triplet)
                    
                    #Moves it to help avoid duplicate triplet results
                    while left < right and nums[left] == triplet[1]:
                        left += 1
                        
                    #Moves it to help avoid duplicate triplet results
                    while left < right and nums[right] == triplet[2]:
                        right -= 1
                  
                #Since we sorted it at the beginning      
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1