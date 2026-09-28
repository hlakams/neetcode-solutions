class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for dict_string, dict_keep in [[s, dict_s], [t, dict_t]]:
            for val in dict_string:
                try:
                    dict_keep[val] += 1
                except:
                    dict_keep.setdefault(val, 1)

        return dict_s == dict_t



        