class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lis=[]
        
    #Appends the element in the list
    def push(self, x: int) -> None:
        return(self.lis.append(x))
        
        
    #returns the last element in the list and pops that element
    def pop(self) -> None:
        return(self.lis.pop())
        
    #returns the last element from the list
    def top(self) -> int:
        return(self.lis[-1])
        
        
    #returns min from the list
    def getMin(self) -> int:
        return(min(self.lis))        
