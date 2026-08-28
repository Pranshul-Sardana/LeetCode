class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []

        #Initiate pointers
        t, b = 0, len(matrix)
        l, r = 0, len(matrix[0])

        #Initiate loops
        while l < r and t < b:

            #Left to right
            for i in range(l, r):
                out.append(matrix[t][i])
            t += 1

            #Top to down
            for i in range(t,b):
                #print(f"{i =}", r-1)
                out.append(matrix[i][r-1])
            r -= 1

            #If ptr overlapped, break
            if not (l < r and t < b):
                break

            #Right to left
            for i in range(r-1,l-1,-1):
                #print(b-1,i)
                out.append(matrix[b-1][i])
            b -= 1
            
            #Bottom to top
            for i in range(b-1,t-1,-1):
                out.append(matrix[i][l])
            l += 1
            
        return out
            