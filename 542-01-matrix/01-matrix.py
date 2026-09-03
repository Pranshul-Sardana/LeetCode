#from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        out_matrix = [[0]*cols for _ in range(rows)]
       
        #Define directions to move
        directions = [[-1,0], [1,0], [0,-1], [0, 1]]

        visited = set()
        queue = deque()
        #Find the locations of 0. 
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    visited.add((r,c))
                    queue.append((r,c))
        print(visited)

        #distance = 0
        #Iterate through the dequqe:
        while len(queue) > 0:
            r, c = queue.popleft()
            distance = out_matrix[r][c] + 1

            #For every elemet, move in all 4 directions (valid only)
            for dr, dc in directions:
                dr += r
                dc += c 

                print(dr,dc)
                #Check invalid and visited
                if (((dr,dc) in visited) or not (0 <= dr < rows)
                    or not (0 <= dc < cols)):
                    continue

                out_matrix[dr][dc] = distance
                
                visited.add((dr,dc))
                queue.append((dr,dc))

        return out_matrix
                
            #Increase the distance from the nearest 0