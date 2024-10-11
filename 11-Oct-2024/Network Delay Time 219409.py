# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,d in times:
            graph[u].append([v,d])
        distances = {i: float('inf') for i in range(1,n+1)}
        distances[k] = 0
        processed = set()
        ans = 0
        heap = [(0, k)]
        while heap:
            cost, curr = heapq.heappop(heap)
            if curr in processed:
                continue
            processed.add(curr)
            
            distances[curr] = cost
            
            for neighbor, weight in graph[curr]:
                ans += (cost + weight)
                distance = cost + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        return max(distances.values()) if len(processed)==n else -1
        