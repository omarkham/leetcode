from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_index, cookie_index = 0, 0
        content_children = 0

        # Iterate through both lists
        while child_index < len(g) and cookie_index < len(s):
            # if cookie size is good for current child
            if s[cookie_index] >= g[child_index]:
                # assign and move to next child
                content_children += 1
                child_index += 1
                cookie_index += 1
            else:
                # if it's not good, move to the next one
                cookie_index += 1

        return content_children
