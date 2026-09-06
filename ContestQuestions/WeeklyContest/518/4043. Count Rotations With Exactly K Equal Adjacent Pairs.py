class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        count = 0 # for circular array!
        for i in range(n):
            if s[i] == s[(i+1) % n]:
                count+=1
        ans = 0
        if k == count-1:
            ans += count
        if k == count:
            ans += (n-count)
        return ans