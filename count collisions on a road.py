class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L')
        directions = directions.rstrip('R')
        collisions = 0
        for c in directions:
            if c != 'S':  
                collisions += 1
        return collisions
        
