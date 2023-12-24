class Solution:
    def minOperations(self, s: str) -> int:
        
        pattern_1_count = 0 #01010..
        pattern_2_count = 0 #10101..

        for i, char in enumerate(s):
            
            expected_char_pattern_1 = '0' if i%2 == 0 else '1' #if it's even vs. odd
            expected_char_pattern_2 = '1' if i%2 == 0 else '0'

            if char != expected_char_pattern_1:
                pattern_1_count += 1
            if char != expected_char_pattern_2:
                pattern_2_count += 1

        return min(pattern_1_count, pattern_2_count)

