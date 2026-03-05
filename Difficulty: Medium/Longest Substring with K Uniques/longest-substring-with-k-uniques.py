#user function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        m,c,ma = -1, "",{}
        for i in s:
            c += i
            # ma[i] = 1 + ma.get(ma[i],0)
            if i not in ma: ma[i] = 1
            else: ma[i] += 1
            if len(ma) == k: m = max(m,len(c))
            elif len(ma) > k: 
                ma[c[0]] -= 1
                if ma[c[0]] == 0: del ma[c[0]]
                c = c[1:]
        return m

