class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        
        for idx in range(min(len(word1), len(word2))):
            ans += word1[idx]
            ans += word2[idx]
        
        if len(word1) < len(word2):
            ans += word2[len(word1):]
        if len(word2) < len(word1):
            ans += word1[len(word2):]
        
        return ans