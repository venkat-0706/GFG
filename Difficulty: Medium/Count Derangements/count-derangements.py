class Solution:
    def derangeCount(self, n: int) -> int:
        if n == 1: return 0
        if n == 2: return 1
        a, b = 0, 1
        for i in range(3, n + 1):
            a, b = b, (i - 1) * (b + a)
        return b