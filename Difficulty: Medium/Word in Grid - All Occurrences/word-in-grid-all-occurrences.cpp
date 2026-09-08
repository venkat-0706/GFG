class Solution {
  public:
    int n;
    int m;
    int row[8] = {-1,-1,0,1,1,1,0,-1};
    int col[8] = {0,1,1,1,0,-1,-1,-1};

    bool check(int i,int j){
        return i>=0 && j>=0 && i<n && j<m;
    }


    int DFS(int i,int j,vector<vector<char>> &mat, string &word){

        int s = word.size();

        for(int dir=0;dir<8;dir++){
            int i1 = i;
            int j1 = j;
            int index = 1;
            if(!check(i1+(row[dir]*(s-1)),j1+(col[dir]*(s-1))))continue;

            while(check(i1+row[dir],j1+col[dir]) && (index<s) && (mat[i1+row[dir]][j1+col[dir]]==word[index])){
                index++;
                i1 = i1+row[dir];
                j1 = j1+col[dir];
            }

            if(index==s)return 1;
        }

        return 0;

    }

    vector<vector<int>> searchWord(vector<vector<char>> &mat, string &word) {
        // Code here
        n = mat.size();
        m = mat[0].size();
        vector<vector<int>>ans;

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){

                if(mat[i][j]==word[0] && DFS(i,j,mat,word))ans.push_back({i,j});

            }
        }


        return ans;

    }
};