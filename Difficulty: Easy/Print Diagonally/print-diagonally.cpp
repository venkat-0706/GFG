class Solution {
  public:
    virtual void fun(int i, int j, int n, vector<vector<int>> mat, vector<int> &ans){
      while(i<n && j>=0){
        ans.push_back(mat[i][j]);
        i++; j--;
      }
      return;
    }
    
    virtual vector<int> diagView(vector<vector<int>> mat){
      vector<int> ans;
      int n=mat.size();
      for(int j=0; j<n; j++){
        fun(0, j, n, mat, ans);  
      }      
      for(int i=1; i<n; i++){
        fun(i, n-1, n, mat, ans);  
      }
      
      return ans;
    }
};