import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [ [enqueueTime, processingTime, index] for index, [enqueueTime, processingTime] in enumerate(tasks)]
        tasks = sorted( tasks, key = lambda x : x[0] )
        res = []
        heap = []
        i = 0
        t = 0
        while i<len(tasks)  or heap:
            if not heap and t<tasks[i][0]:
                t = tasks[i][0]

            while i<len(tasks) and t>=tasks[i][0]:
                heapq.heappush(heap, ( tasks[i][1], tasks[i][2] ))
                i+=1

            if heap:
                pt, idx = heapq.heappop(heap)
                res.append(idx)
                t+=pt

        return res