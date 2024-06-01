class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonStr=""
        for string in zip(*strs):
            if len(set(string)) == 1:
                commonStr+=string[0]
            else:
                return commonStr
        return commonStr
