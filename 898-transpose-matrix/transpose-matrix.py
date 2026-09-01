class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        out_matrix = [[0]*rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                out_matrix[c][r] = matrix[r][c]

        return out_matrix