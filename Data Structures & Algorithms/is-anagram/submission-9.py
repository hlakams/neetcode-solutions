class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for dict_string, dict_keep in [(s, dict_s), (t, dict_t)]:
            for val in dict_string:
                dict_keep[val] = dict_keep.get(val, 0) + 1
        
        return dict_s == dict_t