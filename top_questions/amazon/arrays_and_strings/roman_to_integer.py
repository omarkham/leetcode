from typing import List

class Solution:
    def RomanToInt(self, s:str) -> int:
        
        dictionary = {
        "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
        "XL": 40, "L": 50, "XC": 90, "C": 100,
        "CD": 400, "D": 500, "CM": 900, "M": 1000
        }
        
        result = 0
        i = 0
        while i < len(s):
            #check for two-character Roman numeral
            if i + 1 < len(s) and s[i:i + 2] in dictionary:
                result += dictionary[s[i:i + 2]]
                i += 2 # move to the next pair
            else:
                result += dictionary[s[i]]
                i += 1 # move to the next character
                
        return result




#Test
solution_instance = Solution()

input_string = "MCMXCIV"
result = solution_instance.RomanToInt(input_string)

print("Result:", result)
