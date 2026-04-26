class Solution:
    def commonElements(self, a, b, c):
        ret=[None]
        if len(a)>len(b):
            a,b=b,a
        if len(a)>len(c):
            a,c=c,a
        ib=len(b)-1
        ic=len(c)-1
        for ia in range(len(a)-1,-1,-1):
            if a[ia]==ret[-1]:
                continue
            while ib>0 and b[ib]>a[ia]:
                ib-=1
            while ic>0 and c[ic]>a[ia]:
                ic-=1
            if a[ia]==b[ib] and a[ia]==c[ic]:
                ret.append(a[ia])
        return ret[1:][::-1]