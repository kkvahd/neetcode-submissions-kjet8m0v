class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append(curr.copy())
                return

            if openN < n:
                curr.append("(")
                dfs(openN + 1, closedN)
                curr.pop()

            if closedN < openN:
                curr.append(")")
                dfs(openN, 1 + closedN)
                curr.pop()

        dfs(0, 0)
        return [''.join(i) for i in res]