class Solution {
  public:
    int shortestPath(vector<vector<int>> &mat) {
        // code here
        int n = mat.size(), m = mat[0].size();
        vector<vector<int>> matrix(n, vector<int>(m, 1));

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(mat[i][j] == 0){
                    matrix[i][j] = 0;
                    int dx[4] = {-1, 0, 1, 0};
                    int dy[4] = {0, 1, 0, -1};

                    for(int k=0; k<4; k++){
                        int newX = dx[k] + i;
                        int newY = dy[k] + j;

                        if(newX >= 0 && newX < n && newY >= 0 && newY < m){
                            matrix[newX][newY] = 0;
                        }
                    }
                }
            }
        }

        vector<vector<int>> visited(n, vector<int>(m, 0));
        queue<pair<pair<int, int>, int>> q;

        for(int i=0; i<n; i++){
            if(matrix[i][0] == 1){
                q.push({{i, 0}, 1});
                visited[i][0] = 1;
            }
        }

        while(!q.empty()) {
            pair<pair<int, int>, int> p = q.front();

            int x = p.first.first;
            int y = p.first.second;
            int count = p.second;
            q.pop();

            if(y == m-1) return count;

            int dx[4] = {-1, 0, 1, 0};
            int dy[4] = {0, 1, 0, -1};

            for(int k=0; k<4; k++){
                int newX = dx[k] + x;
                int newY = dy[k] + y;

                if(newX >= 0 && newX < n && newY >= 0 && newY < m && matrix[newX][newY] == 1 && visited[newX][newY] == 0){
                    q.push({{newX, newY}, count+1});
                    visited[newX][newY] = 1;
                }
            }
        }
        return -1;
    }
};