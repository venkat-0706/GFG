class Solution:
    def overlapInt(self, arr):
        from collections import defaultdict
        count = defaultdict(int)
        for sta , sto in arr :
            count[sta] += 1
            count[sto+1] -= 1
        max_sum = curr_sum = 0
        for ix in sorted(count):
            curr_sum += count[ix]
            max_sum = max(max_sum , curr_sum)
        return max_sum
