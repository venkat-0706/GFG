class Solution:
    def isWordExist(self, mat, word):
        hth=len(mat)
        wth=len(mat[0])
        seen=set()
        def dfs(x,y,ix=len(word)-1):
            nonlocal mat,hth,wth,word,seen
            if ix==0:
                if mat[y][x]==word[ix]:
                    return True
            if mat[y][x]!=word[ix]:
                return False
            seen.add((x,y,))
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx=x+dx
                ny=y+dy
                if not (0<=nx<wth and 0<=ny<hth) or (nx,ny,) in seen:
                    continue
                if dfs(nx,ny,ix-1):
                    return True
            seen.discard((x,y,))
            return False
        for y in range(hth):
            for x in range(wth):
                seen.clear()
                if dfs(x,y):
                    return True
        return False
