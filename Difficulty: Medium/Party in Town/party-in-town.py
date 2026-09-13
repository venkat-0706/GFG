from collections import deque

class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        def bfs(start):
            n = len(adj)
            dist = [-1] * n
            q = deque()

            dist[start] = 0
            q.append(start)

            farthest_node = start
            farthest_dist = 0

            while q:
                node = q.popleft()

                for next_node in adj[node]:
                    next_node -= 1

                    if dist[next_node] == -1:
                        dist[next_node] = dist[node] + 1
                        q.append(next_node)

                        if dist[next_node] > farthest_dist:
                            farthest_dist = dist[next_node]
                            farthest_node = next_node

            return farthest_node, farthest_dist

        diameter_end, _ = bfs(0)
        _, diameter = bfs(diameter_end)

        return (diameter + 1) // 2