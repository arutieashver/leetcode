class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            result = []
            stack = [('', 0, 0)]  

            while stack:
                s, left, right = stack.pop()
                if len(s) == 2 * n:
                    result.append(s)
                if left < n:
                    stack.append((s + '(', left + 1, right))
                if right < left:
                    stack.append((s + ')', left, right + 1))

            return result