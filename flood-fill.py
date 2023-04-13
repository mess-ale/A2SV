class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        vis = set()
        given = image[sr][sc]
        def inbound(row, col):
            return 0<=row<len(image) and 0<=col<len(image[0]) and (row, col) not in vis

        def helper(row, col, visited, dir, color):
            
            visited.add((row, col))
            for i in dir:
                new_row = row + i[0]
                new_col = col + i[1]
                image[row][col] = color
                if inbound(new_row, new_col) and image[new_row][new_col] == given:
                    helper( new_row, new_col, visited, dir, color)

        
        helper(sr, sc, vis, dir, color)
        return image