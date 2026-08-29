import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": lambda a, b: int(a / b)}
        for ele in tokens:
            if ele.lstrip('-').isdigit() and ele != '-':
                stack.append(int(ele))
            elif ele in operators:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(operators[ele] (op2, op1))
        return stack[-1]