class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        if rows*cols != r*c:
            return mat

        out_matrix = [[0]*c for _ in range(r)]

        for r_item in range(rows):
            for c_item in range(cols):
                index = r_item*cols+c_item
                out_matrix[index//c][index%c] = mat[r_item][c_item]

        return out_matrix