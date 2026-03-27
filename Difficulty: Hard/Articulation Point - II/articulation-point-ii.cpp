class Solution {
    private:
    void GET_DFS(int node, vector<int> &disc, vector<int> &low, vector<int> &vis, vector<int> &art, vector<int> adj[], int &timer, int parent){
        vis[node]=1;
        low[node]=disc[node]=timer;
        int count=0;
        for(auto i: adj[node]){
            if(i==parent)continue;
            if(vis[i]){
                low[node]= min(low[node], disc[i]);
            }
            else{
                timer++;
                count++;
                GET_DFS(i,disc, low, vis, art, adj, timer, node);
                if(low[i]>=disc[node] and parent!=-1){
                    art[node]=1;
                }
                low[node]= min(low[node], low[i]);
            }
            if(count>1 and parent==-1)
            art[node]=1;
        }
    }
  public:
    vector<int> articulationPoints(int V, vector<vector<int>>& edges) {
        // Code here
        vector<int> disc(V, 0);
        vector<int> low(V, 0);
        vector<int> art(V, 0);
        vector<int> vis(V, 0);
        vector<int> ans;
        vector<int> adj[V];
        for(int i=0; i<edges.size(); i++){
            int u= edges[i][0];
            int v= edges[i][1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        int timer=0;
        for(int i=0; i<V; i++){
            if(!vis[i]){
                GET_DFS(i, disc, low, vis, art, adj, timer, -1);
            }
        }
        for(int i=0; i<V; i++)
        if(art[i]==1)ans.push_back(i);
        if(ans.empty())return {-1};
        return ans;
    }
};