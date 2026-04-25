class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        i = 0
        res = 0
        for c in moves:
            if c =='_':
                i+=1
            elif c == 'L':
                res-=1
            else:
                res+=1
        return abs(res) + i
        