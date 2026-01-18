class Solution:
    def removeKdig(self, s, k):
        if len(s)==k:
            return '0'
        stk=[]
        for ix,c in enumerate(s):
            while stk and stk[-1]>c:
                stk.pop()
                k-=1
                if k==0:
                    stk.extend(s[ix:])
                    break
            if k==0:
                break
            stk.append(c)
        if k>0:
            stk=stk[:-k]
        for ix,c in enumerate(stk):
            if c!='0':
                break
        return ''.join(stk[ix:])