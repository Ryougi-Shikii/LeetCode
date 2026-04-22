class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        from heapq import heappush, heappop
        def EDToO(point):
            x, y = point
            return sqrt((x*x) + (y*y))
        heap = []
        for point in points:
            heappush(heap, ( -EDToO(point), point ))
            if len(heap) > k:
                heappop(heap)
        return [x for _,x in heap]
        
        
        