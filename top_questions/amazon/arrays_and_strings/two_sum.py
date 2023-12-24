from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i

        return []


#Test
solution_instance = Solution()

nums_example = [2, 7, 11, 15]
target_example = 9
result = solution_instance.twoSum(nums_example, target_example)

print("Result:", result)
