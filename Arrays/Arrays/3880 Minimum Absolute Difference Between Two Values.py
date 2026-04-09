class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        mini = 1001
        one = []
        two = []
        for i,num in enumerate(nums):
            if num == 1:
                one.append(i)
            if num == 2:
                two.append(i)
        for i in one:
            for j in two:
                mini = min(mini, abs(i-j))
        if mini==1001:
            return -1
        return mini
        
            