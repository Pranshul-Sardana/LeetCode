class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # Will be used to set column to 0

                    #Make first element of each row 0
                    if r == 0:
                        rowZero = True
                    else:
                        matrix[r][0] = 0

        #Setting 0 for everything except the 0th row and column
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        #Check first colums
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        #Check first row
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0

        return matrix