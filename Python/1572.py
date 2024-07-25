class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output = 0
        c = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i, j) not in c:
                    if i == j:
                        output += mat[i][j]
                        c.add((i,j))
                    elif i + j == len(mat) - 1:
                        output += mat[i][j]
                        c.add((i, j))
        return output
    
    
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    output += mat[i][j]
                elif i + j == len(mat) - 1:
                    output += mat[i][j]
       
        
        return output
        