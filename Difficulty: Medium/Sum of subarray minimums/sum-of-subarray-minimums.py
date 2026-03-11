class Solution:
     def sumSubMins(self, arr):
        n = len(arr)
        s = [(0, -1)]
        total = 0
        for end, a in enumerate(arr):
            while s[-1][0] >= a:
                local_min, mid = s.pop()
                total += (mid - s[-1][1]) * local_min * (end - mid)
            s.append((a, end))
        while len(s) > 1:
            local_min, mid = s.pop()
            total += (mid - s[-1][1]) * local_min * (n - mid)
        return total