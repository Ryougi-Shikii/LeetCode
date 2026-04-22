class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heapify, heappush, heappop
        dic = {  }
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        res = [] # k most frequent
        for i, j in dic.items():
            heappush(res, (-j, i))
        
        ans = []
        for _ in range(k):
            ans.append(heappop(res)[1])

        return ans