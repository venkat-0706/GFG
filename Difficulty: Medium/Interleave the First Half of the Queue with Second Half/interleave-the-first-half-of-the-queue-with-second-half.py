from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        h = []
        while q:
            h.append(q.popleft())
        for i in range(n // 2):
            q.append(h[i])
            q.append(h[i + n // 2])