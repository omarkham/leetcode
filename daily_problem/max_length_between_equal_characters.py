class Solution:
    def maxLengthBetweenEqualCharacters(self, s:str) -> int:
        
        #dict to store character and index where it is
        #for example {"a": 0, "b": 1}. so char maps to index
        seen = {}
        max_dist = -1
        
        for i, char in enumerate(s):
            #then we can have a distance between the two identical chars in s
            if char in seen:
                '''print(i)
                print(seen[char])
                print("\n")'''
                dist = i - seen[char] -1
                if dist > max_dist:
                    max_dist = dist
            else:
                seen[char] = i
            
        return max_dist
    
    
#issues: what if there are multiple of the same character in the string? doesn't matter    

#Test
solution_instance = Solution()

input_string = "mgntdygtxrvxjnwksqhxuxtrv"
result = solution_instance.maxLengthBetweenEqualCharacters(input_string)

print("Result:", result)
            
'''
6
1


7
3


11
8


13
2


19
8


21
8


22
3


23
9


24
10


Result: 18
'''           