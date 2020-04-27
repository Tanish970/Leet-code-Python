class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row=len(matrix)
        if row==0:return 0
        h=0
        col=len(matrix[0])
        dupmat=[[0 for i in range(col+1)] for j in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                if matrix[i-1][j-1]=="1":
                    dupmat[i][j]=1+(min(int(dupmat[i-1][j]),int(dupmat[i][j-1]),int(dupmat[i-1][j-1])))
                    h=max(h,dupmat[i][j])
        return h**2
