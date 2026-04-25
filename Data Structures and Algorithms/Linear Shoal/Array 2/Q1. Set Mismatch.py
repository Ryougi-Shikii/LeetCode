class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count = [0]*(n+1)

        for i in nums:
           count[i]+=1

        for i in range(1,1+n):
            if count[i]==2:
                duplicate=i
            elif count[i]==0:
                missing=i

        return [duplicate,missing]