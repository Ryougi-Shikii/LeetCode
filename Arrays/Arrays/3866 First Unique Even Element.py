class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                val=nums[i]
                count=0
                for i in range(len(nums)):
                    if nums[i]==val:
                        count+=1
                print(count)
                if count==1:
                    return val
        return -1
        