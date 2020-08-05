class Solution:
    def trap(self, height: List[int]) -> int:
        le=len(height)
        ans=0
        if le==1 or le==0:return 0
        a=[0]*le
        a[0]=height[0]
        b=[0]*le
        b[le-1]=height[le-1]
        for i in range(1,le):
            a[i]=max(height[i],a[i-1])
            b[le-i-1]=max(height[le-1-i],b[le-i])
        for i in range(le):
            ans+=min(a[i],b[i])-height[i]
        return ans
        
