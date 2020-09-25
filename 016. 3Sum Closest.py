class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        cl=sum(nums[0:3])
        if len(nums)==3:return sum(nums)
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while(l<r):
                s=nums[i]+nums[l]+nums[r]
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    return target
                cl=cl if (min(abs(target-s),abs(target-cl))==abs(target-cl)) else s
                
        return cl
            
        
        
