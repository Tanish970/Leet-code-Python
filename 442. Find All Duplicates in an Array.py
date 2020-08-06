from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        res=[key for key in c if c[key]>1]
        return res
