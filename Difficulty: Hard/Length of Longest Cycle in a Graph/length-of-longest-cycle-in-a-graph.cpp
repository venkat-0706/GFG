class Solution {
  public:
    int longestCycle(int V, vector<vector<int>>& edges) {
        // code here
        vector<vector<int>> adj(V);
        for(auto it : edges)
        {
            adj[it[0]].push_back(it[1]);
        }
        vector<int> dis(V,0);
        vector<bool> vis(V,false);
        unordered_set<int> st;
        int cycle = -1;
        function<void(int)> dfs = [&](int node){
            vis[node] = true;
            st.insert(node);
            for(int child : adj[node])
            {
                if(!vis[child])
                {
                    dis[child] = dis[node] + 1;
                    dfs(child);
                }
                else 
                {  
                    if(st.find(child) != st.end())
                    cycle = max(cycle,abs(dis[child]-dis[node])+1);
                }
            }
        };
      
        for(int i = 0;i<V;i++)
        {
            if(!vis[i])
            dfs(i);
            st.clear();
        }
        return cycle;
        
    }
};

