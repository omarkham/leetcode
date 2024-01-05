class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        subsequence = []
        
        for num in nums:
            #find the idx where num should be inserted into the list to maintain its sorted order
            prev_idx = bisect_left(subsequence, num)
            
            if prev_idx == len(subsequence):
                #means num is greater than all elements in the current subsequence
                subsequence.append(num)
            else:
                #num can replace an existing element in the subsequence to extend the increasing subsequence
                subsequence[prev_idx] = num

        result = len(subsequence)
        del subsequence #deletes the list to free up memory
        return result