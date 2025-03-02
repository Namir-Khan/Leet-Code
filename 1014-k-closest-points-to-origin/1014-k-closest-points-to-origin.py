class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for (x, y) in points:
            dist = -sqrt((x*x + y*y)) # Here we add a -ve sign to make this max-heap

            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y)) # Note we are using max-heap but even tho we need min dist
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x, y) for (dist, x, y) in heap]