class Solution:
    def smallestDiff(self,a, b, c):
        a.sort()
        b.sort()
        c.sort()
        i,j,k=0,0,0
        n=len(a)
        ans=float('inf')
        while i<n and j<n and k<n:
            maxi=max(a[i],b[j],c[k])
            mini=min(a[i],b[j],c[k])
            if ans>maxi-mini:
                res=[a[i],b[j],c[k]]
                ans=maxi-mini
            if mini==a[i]:
                i += 1
            elif mini==b[j]:
                j += 1
            else:
                k += 1
        res.sort(reverse=True)
        return res