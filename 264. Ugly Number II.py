class Solution:
    def nthUglyNumber(self, n: int) -> int:
        f,k=[2,3,5],3
        l,s=[1],[0]*k
        for i in range(n-1):
            c=[f[i]*l[s[i]] for i in range(k)]
            new_one=min(c)
            l.append(new_one)
            s=[s[i]+(c[i]==new_one) for i in range(k)]
        return l[-1]
