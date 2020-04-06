class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)  
        for j in range(len(A)-2):
            if A[j+1]+A[j+2] > A[j]:
                return sum([A[i] for i in range(j, j+3)])
        return 0
            
