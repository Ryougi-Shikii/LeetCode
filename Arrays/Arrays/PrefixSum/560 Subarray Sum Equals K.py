class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix = [0]
        # for num in nums:
        #     prefix.append(prefix[-1]+num)

        freq = {0:1}
        prefix = 0
        answer = 0

        for num in nums:
            prefix += num
            answer += freq.get(prefix - k, 0)
            freq[prefix] = freq.get(prefix, 0) + 1

        return answer