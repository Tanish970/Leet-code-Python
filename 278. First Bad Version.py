class Solution:
    def firstBadVersion(self, n):
        l,r=1,n
        while(l<=r):
            mid=(l+r)//2
            if isBadVersion(mid):
                r=mid-1
            else:
                l=mid+1
        if isBadVersion(l):return l
        return l-1
