class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))

        min_heap = [(0, k)] # Heap to get the shortest path
        visited = set()
        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            # Now BFS to visit neighbours
            for w2, n2 in adj[n1]:
                if not n2 in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))

        return t if len(visited) == n else -1 # O(E * logV)