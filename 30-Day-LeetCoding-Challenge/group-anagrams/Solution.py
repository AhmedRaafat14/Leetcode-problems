class Solution:
    def groupAnagrams(self, strs):
        anagramsMapper = {}

        for word in strs:
            key = "".join(sorted(word))
            anagramsMapper[key] = anagramsMapper.get(key, []) + [word]

        return anagramsMapper.values()


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
