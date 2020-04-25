def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:return 0
        rows,col=len(grid),len(grid[0])
        for r in range(rows):
            for c in range(col):
                if r==0 and c==0:continue#To Avoid (0,0) Pos
                if r==0:grid[r][c]+=grid[r][c-1]#Calculate Row wise
                elif c==0:grid[r][c]+=grid[r-1][c]#To Calculate Col wise
                else:grid[r][c]+=min(grid[r-1][c],grid[r][c-1])
        return grid[rows-1][col-1]
        
#Runtime: 96 ms, faster than 89.01% of Python3 online submissions for Minimum Path Sum.
#Memory Usage: 15.5 MB, less than 17.54% of Python3 online submissions for Minimum Path Sum.
