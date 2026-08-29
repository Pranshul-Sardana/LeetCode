class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        r_set, c_set = set(), set()
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    r_set.add(r)
                    c_set.add(c)

        for r in r_set:
            for c in range(cols):
                matrix[r][c] = 0

        for c in c_set:
            for r in range(rows):
                matrix[r][c] = 0

        return matrix