from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = len(g) - 1
        m = len(s) - 1
        count = 0
        while l>-1 and m>-1:
            if g[l]<=s[m]:
                l-=1
                m-=1
                count+=1
            else:
                l-=1
        return count
