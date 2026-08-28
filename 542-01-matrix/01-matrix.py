class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #Inititate Queue and visited locations
        rows, cols = len(mat), len(mat[0])
        out = [[0]*cols for _ in range(rows)]
        q = deque()
        visited = set()

        #Find locations with 0 and add them to the queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        #Go through the queue, visit the neighbours, and update the value
        #Edge cases 1: Neighbour already visited
        #Edge case 2: Boarder location. Hence, not neighbours
        while q:
            r, c = q.popleft()
            neighbours = [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]
            
            #print(f"0: {r = }, {c = }, {h = }")
            for nr, nc in neighbours:
                if (nr < 0 or nc < 0 or nr == rows or nc == cols
                or (nr, nc) in visited):
                    continue
                
                #print(f"{r = }, {c = }, {h = }")
                out[nr][nc] = out[r][c] + 1
                q.append((nr, nc))
                visited.add((nr,nc))

        return out



