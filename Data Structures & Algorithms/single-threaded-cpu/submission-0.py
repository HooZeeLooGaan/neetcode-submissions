import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_queue = []

        for i, (enqueue_time, processing_time) in enumerate(tasks):
            task_queue.append((enqueue_time, processing_time, i))

        task_queue.sort(key = lambda x: x[0])

        task_pool = []
        seq = []
        k = 0
        i = 0
        n = len(task_queue) 
        
        while i < n or task_pool:
            if not task_pool and k < task_queue[i][0]:
                k = task_queue[i][0]

            while i < n and k >= task_queue[i][0]:
                task = task_queue[i]
                heapq.heappush(task_pool, (task[1], task[2]))
                i += 1

            excecution_time, index = heapq.heappop(task_pool)
            k += excecution_time
            seq.append(index)

        return seq
