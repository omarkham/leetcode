class Solution:
    def isPathCrossing(self, path: str) -> bool:

        x = 0
        y = 0

        visited = set([(x,y)])

        for move in path:
            if move == "N":
                y += 1
            elif move == "S":
                y -= 1
            elif move == "E":
                x += 1
            else:
                x -= 1
            
            if (x,y) in visited:
                return True

            visited.add((x, y))
        
        return False
        