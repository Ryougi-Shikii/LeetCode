class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        # s = ''.join(map(str, nums))
        # return s.count(str(digit))
        count = 0
        for num in nums:
            if str(digit) in str(num):
                count += str(num).count(str(digit))
        return count
    
