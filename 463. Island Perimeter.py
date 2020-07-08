class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid)==0:return 0
        res=0
        grid=[[0]*len(grid[0])]+grid+[[0]*len(grid[0])]
        grid=[[0]+grid[i]+[0] for i in range(len(grid))]
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j]==1:
                    if grid[i-1][j]==0:res+=1
                    if grid[i+1][j]==0:res+=1
                    if grid[i][j-1]==0:res+=1
                    if grid[i][j+1]==0:res+=1
        return res
