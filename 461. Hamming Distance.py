class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x==y:return 0
        c=bin(x^y)
        return c.count('1')
