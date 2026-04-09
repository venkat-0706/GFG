class Solution:
    def intersection(self,a, b):
        return sorted(list(set(a) & set(b)))