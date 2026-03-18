/*
class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int x) {
        data = x;
        left = right = nullptr;
    }
};
*/

class Solution {
  public:
    virtual int dfs(Node *r, int &ans){
      if(!r) return 0;
      
      int left=dfs(r->left, ans);
      int right=dfs(r->right, ans);
      
      ans += (abs(left)+abs(right));
      return (r->data)+left+right-1;
    }
    
    
    virtual int distCandy(Node* root){
      int ans=0;
      dfs(root, ans);
      return ans;
    }
};