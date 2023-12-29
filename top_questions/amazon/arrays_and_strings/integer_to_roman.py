from typing import List

class Solution:
    def intToRoman(self, num: int) -> str:
        
        dictionary = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
            40: "XL", 50: "L", 90: "XC", 100: "C",
            400: "CD", 500: "D", 900: "CM", 1000: "M"
        }
        
        '''print(sorted(dictionary.keys(), reverse=True))'''
        
        result = ""
        #iterates over the keys of the dictionary in descending order
        #this ensures that we start with the largest possible values
        for value in sorted(dictionary.keys(), reverse=True):
            '''print(f"num: {num}")
            print(f"value: {value}")'''
            #checks how many times the current value can be subtracted from the given integer 'num'
            #this loop continues until the value can no longer be subtracted
            while num >= value:
                '''print(f"num: {num}")
                print(f"value: {value}")
                print(f"result: {result}")'''
                #appends the corresponding roman numeral symbol to the result string
                result += dictionary[value]
                #subtracts the current value from the given integer 'num'
                num -= value
                
        return result




#Test
solution_instance = Solution()

input_number = 58
result = solution_instance.intToRoman(input_number)

print("Result:", result)


#example:
'''
[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
num: 58
value: 1000
num: 58
value: 900
num: 58
value: 500
num: 58
value: 400
num: 58
value: 100
num: 58
value: 90
num: 58
value: 50
num: 58
value: 50
result:
num: 8
value: 40
num: 8
value: 10
num: 8
value: 9
num: 8
value: 5
num: 8
value: 5
result: L
num: 3
value: 4
num: 3
value: 1
num: 3
value: 1
result: LV
num: 2
value: 1
result: LVI
num: 1
value: 1
result: LVII
Result: LVIII
'''