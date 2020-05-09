class Solution(object):
    def checkStraightLine(self, coordinates):
        if len(coordinates)==2:return True
        if (coordinates[1][0]-coordinates[0][0])==0:return False
        slope=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        c=coordinates[0][1]-slope*coordinates[0][0]
        for i in range(2,len(coordinates)):
            if coordinates[i][1]!=slope*coordinates[i][0]+c:return False
        return True
    
