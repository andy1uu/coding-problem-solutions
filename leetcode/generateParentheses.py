class Solution:

    def generateParentheses(self, n: int) -> List[str]:

        stack = []

        result = []

        def backTrack(openParenNumber: int, closedParenNumber: int):

            if openParenNumber == closedParenNumber == n:
                result.append("".join(stack))
                return

            if openParenNumber < n:
                stack.append("(")
                backTrack(openParenNumber + 1, closedParenNumber)
                stack.pop()

            if closedParenNumber < openParenNumber:
                stack.append(")")
                backTrack(openParenNumber, closedParenNumber + 1)
                stack.pop()

        backTrack(0, 0)

        return result
