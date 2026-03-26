class Solution {

    public int countPaths(int V, int[][] edges) {

       // int mod=1000000009+7;

    List<List<int[]>>adj=new ArrayList<>();

    for(int i=0;i<V;i++)

    adj.add(new ArrayList<>());

    for(int[]e:edges){

        adj.get(e[0]).add(new int[]{e[1],e[2]});

        adj.get(e[1]).add(new int[]{e[0],e[2]});

    }

    long[]dist=new long[V];

    long[]ways=new long[V];

    Arrays.fill(dist,Long.MAX_VALUE);

    PriorityQueue<long[]>pq=new PriorityQueue<>((a,b)->Long.compare(a[0],b[0]));

    dist[0]=0;

    ways[0]=1;

    pq.offer(new long[]{0,0});

    while(!pq.isEmpty()){

        long[]cur=pq.poll();

        long d=cur[0];

        int u=(int)cur[1];

        if(d>dist[u]) continue;

        for(int[]it:adj.get(u)){

            int v=it[0];

            long w=it[1];

        if(dist[v]>dist[u]+w){

            dist[v]=dist[u]+w;

            ways[v]=ways[u];

        pq.offer(new long[]{dist[v],v});

        }else if(dist[v]==dist[u]+w){

            ways[v]=(ways[u]+ways[v]);

        }

        }

    }

    return (int)(ways[V-1]);

    }

}