class Solution:
    POWERS_OF_2 = {2**i: i + 1 for i in range(31)}
    
    def findPosition(self, n):
        return self.POWERS_OF_2.get(n, -1)