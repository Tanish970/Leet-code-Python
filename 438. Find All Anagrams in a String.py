class Solution(object):
    def findAnagrams(self, s, p):
        les,lep=len(s),len(p)
        p=Counter(p)
        a=Counter()
        b=[]
        for i in range(les):
            a[s[i]]+=1
            if i>=lep:
                if a[s[i-lep]]==1:
                    del a[s[i-lep]]
                else: a[s[i-lep]]-=1
            if a==p:
                b.append(i-lep+1)
        return b
            
