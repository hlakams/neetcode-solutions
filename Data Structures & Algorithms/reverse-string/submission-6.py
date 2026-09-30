class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)

        for idx in range(0, len_s // 2):
            swap = s[idx]
            trail_idx = len_s - idx - 1

            if s[idx] == trail_idx:
                continue
            else:
                s[idx] = s[trail_idx]
                s[trail_idx] = swap
            