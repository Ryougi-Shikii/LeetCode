class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n+1)
        for i in nums:
            count[i] += 1
        return [i for i in range(1, n+1) if count[i]<1]
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        set1 = set(nums)
        set2 = set(range(1, n+1))
        for i in list(set1):
            set2.remove(i)
        return list(set2)
"""