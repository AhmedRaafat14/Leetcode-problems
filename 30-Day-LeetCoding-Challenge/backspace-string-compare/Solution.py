class Solution:
    def backspaceCompare(self, S, T):
        def helper(st):
            ans = []
            for ch in st:
                if ch != '#':
                    ans.append(ch)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return helper(S) == helper(T)

if __name__ == "__main__":
    sol = Solution()
    print(sol.backspaceCompare("ab#c", "ad#c"))
    print(sol.backspaceCompare("ab##", "c#d#"))
    print(sol.backspaceCompare("a##c", "#a#c"))
    print(sol.backspaceCompare("a#c", "b"))
