from typing import List

#sliding window approach. window expands or contracts as the algorithm iterates through the string
#window is start_index to end_index

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_indices = {} #dict to store the index of each character
        max_length = 0 #max length of the substring
        start_index = 0 #start index of the current substring
        
        #end_index is to represent the endpoint of the current substring being considered
        for end_index, char in enumerate(s):
            #if the character is already in the substring
            # (means the character is repeating within the current substring)
            if char in char_indices and char_indices[char] >= start_index:
                #update the start index to the next position after the repeated character
                start_index = char_indices[char] + 1
                
            #update the index of the current character
            char_indices[char] = end_index
            
            #calculate the length of the current substring
            current_length = end_index - start_index + 1
            
            #update the max length
            max_length = max(max_length, current_length)
            
        return max_length
                


#Test
solution_instance = Solution()

input_string = "abcabcbb"
result = solution_instance.lengthOfLongestSubstring(input_string)

print("Result:", result)
