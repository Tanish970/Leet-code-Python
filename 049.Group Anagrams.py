class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=collections.defaultdict(list)
        for i in strs:
            ans[''.join(sorted(i))].append(i)
        return ans.values()
        
        
