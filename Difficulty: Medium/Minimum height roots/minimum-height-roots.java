class Solution {
    public ArrayList<Integer> minHeightRoot(int v, int[][] edges) {
        // Code here
        if (edges == null || v == 0) {
            return new ArrayList<>();
        }
        if (v == 1) {
            return new ArrayList<>(Arrays.asList(edges[0][0]));
        }
        List<List<Integer>> graph = buildGraph(edges, v);
        ArrayList<Integer> result = new ArrayList<>();
        int [] indegree = findIndegree(edges, v);
        bfs(graph, result, indegree);
        return result;
    }
    
    private void bfs(List<List<Integer>> graph, ArrayList<Integer> result, int [] indegree) {
        Queue<Integer> queue = new LinkedList<>();
        for (int node = 0; node < indegree.length; node++) {
            //System.out.println(indegree[node]);
            if (indegree[node] == 1) {
                // this is leaf node, instead of indegree=0. start with indegree=1
                queue.offer(node);
            }
        }
        int remainingNodes = indegree.length;
        while (remainingNodes > 2) {
            int size = queue.size();
            remainingNodes -= size;
            while (size-- > 0) {
                int topNode = queue.poll();
                //remainingNodes --;
                List<Integer> neighbours = graph.get(topNode);
                for (Integer neighbour : neighbours) {
                    indegree[neighbour]--;
                    if (indegree[neighbour] == 1) {
                        queue.offer(neighbour);
                    }
                }
            }
        }
        //System.out.println(queue);
        while (!queue.isEmpty()) {
            result.add(queue.poll());
        }
    }
    
    private int [] findIndegree(int [][] edges, int totalNodes) {
        int [] indegree = new int [totalNodes];
        for (int [] edge : edges) {
            indegree[edge[1]]++;
            indegree[edge[0]]++;
        }
        return indegree;
    }
    
    private List<List<Integer>> buildGraph(int [][] edges, int totalNodes) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int node = 0; node < totalNodes; node++) {
            graph.add(new ArrayList<>());
        }
        for (int [] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        return graph;
    }
}