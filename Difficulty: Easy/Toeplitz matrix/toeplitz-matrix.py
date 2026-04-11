class Solution:
    def isToeplitz(self, mat):
        n = len(mat)
        m = len(mat[0])
        def isValid(x,y):
            return x<n and y<m
        for i in range(0,n):
            for j in range(0,m):
                if isValid(i+1,j+1) and mat[i][j]!=mat[i+1][j+1]:
                    return False
        return True