class Solution:
    def minCost(self, heights, cost):
        def getCost(h):
            total = 0
            for i in range(len(heights)):
                total += abs(heights[i] - h) * cost[i]
            return total

        left = min(heights)
        right = max(heights)

        while left < right:
            mid = (left + right) // 2

            if getCost(mid) <= getCost(mid + 1):
                right = mid
            else:
                left = mid + 1

        return getCost(left)