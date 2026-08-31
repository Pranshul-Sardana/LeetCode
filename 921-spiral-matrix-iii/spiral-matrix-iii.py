class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        out = []

        i = 0
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        r, c = rStart, cStart
        step = 1

        while len(out) < rows*cols:
            
            for step_freq in range(2):
                dr, dc = directions[i]
                for _ in range(step):
                    if (0 <= r < rows and 0 <= c < cols):
                        out.append([r,c])
                    r += dr
                    c += dc
                    
                i = (i+1) % 4
                
            step += 1
            
        return out