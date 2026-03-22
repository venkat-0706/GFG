class Solution {
    public int orangesRot(int[][] mat) {
        // Code here
        int cnt = 0;
        int n = mat.length, m = mat[0].length;
        boolean[][] vis = new boolean[n][m];
        Queue<int[]> q = new ArrayDeque<>();
        
        
        int[][] dirs = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (mat[i][j] == 2) {
                    q.offer(new int[] {i, j, 0});
                    vis[i][j] = true;
                }
                if (mat[i][j] == 1)
                    cnt++;
            }
        }
        
        int time = 0, cf = 0;
        while (!q.isEmpty()) {
            int r = q.peek()[0];
            int c = q.peek()[1];
            int t = q.peek()[2];
            q.poll();
            
            time = Math.max(time, t);
            
            for (int i = 0; i < dirs.length; ++i) {
                int nr = r + dirs[i][0];
                int nc = c + dirs[i][1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && !vis[nr][nc] && mat[nr][nc] == 1) {
                    q.offer (new int[] {nr, nc, t + 1});
                    vis[nr][nc] = true;
                    cf++;
                }
            }
        }
        
        return ((cf != cnt) ? -1 : time);
    }
}