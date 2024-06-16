class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        col=[0]*m
        row=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    col[i]=1
                    row[j]=1
        for i in range(m):
            for j in range(n):
                if col[i]==1 or row[j]==1:
                    matrix[i][j]=0
