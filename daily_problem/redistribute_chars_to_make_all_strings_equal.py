from collections import defaultdict

class Solution:
    
    def makeEqual(self, words: list[str]) -> bool:
        
        joint = ''.join(words) #concatenates all the words in the list into a single string
        set1 = set(joint)
        
        for i in set1:
            if joint.count(i) % len(words) != 0 : return False
        return True
    
    #very slow...
    '''
    def makeEqual(self, words: list[str]) -> bool:
        
        '''
        Let's count each letter occurence. if all the chars are divisible by the number of words 
        in the list, then it works
        '''
        result_dict = self.count_chars_in_words(words)
        N = len(words)
        
        for char, count in result_dict.items():
            if count %N != 0:
                return False
        
        return True
        
    def count_chars_in_words(self, word_list):
        char_count = defaultdict(int) #defaultdict assigns a char to 0 if it doesn't exist (yet)
        
        for word in word_list:
            for char in word:
                char_count[char] += 1
                
        return char_count
    '''
                
#Test
solution_instance = Solution()

input_list = ["ab","a"]
result = solution_instance.makeEqual(input_list)

print("Result:", result)      