class Solution:
    def checkValidString(self, s):
        if not s:
            return True
        paran = []
        stars = []
        for idx, ch in enumerate(s):
            if ch == '(':
                paran.append(idx)
            elif ch == '*':
                stars.append(idx)
            elif ch == ')':
                if paran:
                    paran.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        if len(paran) > len(stars):
            return False

        while paran and stars:
            if paran.pop() > stars.pop():
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkValidString("()"))
    print(sol.checkValidString("(*)"))
    print(sol.checkValidString("(*))"))
