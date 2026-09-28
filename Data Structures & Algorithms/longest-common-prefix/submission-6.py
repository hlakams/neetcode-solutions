class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_strs = sorted(strs)
        max_string = ""

        for idx in range(len(new_strs[0])):
            if new_strs[0][idx] == new_strs[-1][idx]:
                max_string += new_strs[0][idx]
            else:
                break

        return max_string