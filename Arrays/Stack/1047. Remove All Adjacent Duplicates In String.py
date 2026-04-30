class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        def dubRem(s):
            stack = []
            for c in s:
                if not stack:
                    stack.append(c)
                elif c == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        return dubRem(s)