class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        l, r = 0, n
        t, b = 0, n

        matrix = [[0]*n for _ in range(n)]
        
        val = 0
        while l < r and t < b:
            for i in range(l,r):
                val += 1
                matrix[t][i] = val
            t += 1

            if not (l < r and t < b):
                break

            for i in range(t,b):
                val += 1
                matrix[i][r-1] = val
            r -= 1

            for i in range(r-1,l-1,-1):
                val += 1
                matrix[b-1][i] = val
            b -= 1

            for i in range(b-1,t-1,-1):
                val += 1
                matrix[i][l] = val
            l += 1

        return matrix
