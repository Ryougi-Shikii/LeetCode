class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNo = []
        res = 0
        for c in tokens:
            if c not in '+-*/':
                stackNo.append(int(c))
            else:
                op2 = stackNo.pop()
                op1 = stackNo.pop() 
                if c == '+':
                    res = op1 + op2
                elif c == '-':
                    res = op1 - op2
                elif c == '*':
                    res = op1 * op2
                else:
                    res = int(op1 / op2)
                stackNo.append(res)
        return stackNo[-1]
            
            