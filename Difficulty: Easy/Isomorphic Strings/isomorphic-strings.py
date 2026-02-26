class Solution:
    def areIsomorphic(self, s1, s2):
        d, rev  = {} , {}
        for a , b in zip(s1,s2):
            if a in d:
                if d[a]!=b:
                    return False
            else:
                d[a] = b
                if b in rev:
                    if rev[b]!=a:
                        return False
                        
                else:
                    rev[b] = a
        return True
                    