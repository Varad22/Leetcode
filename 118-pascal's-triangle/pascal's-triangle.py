class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows=[[1]]*numRows
        for i in range(numRows):
            rows[i]=rows[i]*(i+1)
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                if len(rows[i])>2 and j>0 and j<(len(rows[i])-1):
                    rows[i][j]= rows[i-1][j]+rows[i-1][j-1]
        return rows
