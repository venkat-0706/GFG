import math

class Solution:
    def minSteps(self, m, n, d):
        # Edge case
        if d == 0:
            return 0
        
        # NEW FIX ⭐
        if d == m or d == n:
            return 1
        
        # Check possibility
        if d > max(m, n) or d % math.gcd(m, n) != 0:
            return -1
        
        def solve(fromCap, toCap, target):
            fromJug = 0
            toJug = 0
            steps = 0
            
            while fromJug != target and toJug != target:
                if fromJug == 0:
                    fromJug = fromCap
                    steps += 1
                
                transfer = min(fromJug, toCap - toJug)
                toJug += transfer
                fromJug -= transfer
                steps += 1
                
                if fromJug == target or toJug == target:
                    break
                
                if toJug == toCap:
                    toJug = 0
                    steps += 1
            
            return steps
        
        return min(solve(m, n, d), solve(n, m, d))