class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(o, c, curr):
            if o == c == n:
                res.append("".join(curr.copy()))
                return
                
            if o < n:
                curr.append("(")
                dfs(o + 1, c, curr)
                curr.pop()

            if c < o:
                curr.append(")")
                dfs(o, c + 1, curr)
                curr.pop()

        dfs(0, 0, [])
        return res
            