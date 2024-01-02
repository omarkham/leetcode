class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        length = len(needle)
        
        for i in range(len(haystack) - length + 1):
            if needle == haystack[i : i + length]:
                return i
        return -1

    
#Test
solution_instance = Solution()

input_string = "abc"
needle = "c"
result = solution_instance.strStr(input_string, needle)

print("Result:", result)      