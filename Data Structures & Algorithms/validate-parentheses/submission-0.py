class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}':'{', ']':'['}
        print(brackets)
        for char in s:
            match char:
                case '(' | '{' | '[':
                    stack.append(char)
                case ')' | '}' | ']':
                    if not stack or stack.pop() != brackets[char]:
                        return False
                case _:
                    pass
        if not stack:
            return True
        return False
