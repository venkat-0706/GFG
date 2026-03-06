
class Solution:
    def minWindow(self, s, p):
        cnt={c:p.count(c) for c in set(p)}
        mn=float('inf')
        ret=''
        left=0
        for right,ve in enumerate(s):
            if ve not in cnt:
                continue
            cnt[ve]-=1
            while max(cnt.values())==0:
                if mn>right-left+1:
                    mn=right-left+1
                    ret=s[left:right+1]
                if s[left] in cnt:
                    cnt[s[left]]+=1
                left+=1
        return ret