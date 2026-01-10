class Solution:
    def _check(self, s1,s2, start):
        n2 = len(s2)
        nextVal = 0
        end = -1
        for i in range(start, len(s1)):
            if s1[i] == s2[nextVal]:
                if nextVal == n2-1:
                    end = i - start + 1
                    return end
                else:
                    nextVal +=1
        return end
    def minWindow(self, s1, s2):
        n1 = len(s1)
        start = 0
        minSubStringEnd = 99999
        for i in range(n1):
            if s1[i] == s2[0]:
                end = self._check(s1,s2, i)
                if end != -1 and end < minSubStringEnd:
                    start = i
                    minSubStringEnd = end

        if minSubStringEnd == 99999:
            return ""
        return s1[start:minSubStringEnd+start]

