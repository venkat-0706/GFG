class Solution:
    def permuteDist(self, arr):
        ret=[]
        cur=[]
        cands=set(arr)
        def backtrack():
            nonlocal ret,cur,cands
            if not cands:
                ret.append(cur[:])
                return
            for cand in list(cands):
                cur.append(cand)
                cands.discard(cand)
                backtrack()
                cur.pop()
                cands.add(cand)
        backtrack()
        return ret