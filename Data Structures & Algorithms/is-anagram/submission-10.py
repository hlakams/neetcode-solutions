class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for idx in range(len(s)):
            dict_s[s[idx]] = dict_s.get(s[idx], 0) + 1
            dict_t[t[idx]] = dict_t.get(t[idx], 0) + 1
        
        return dict_s == dict_t