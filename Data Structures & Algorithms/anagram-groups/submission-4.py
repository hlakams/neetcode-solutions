class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}

        for val in strs:
            new_val = "".join(sorted(val))
            if new_val in sorted_dict:
                sorted_dict[new_val].append(val)
            else:
                sorted_dict[new_val] = [val]
        
        return list(sorted_dict.values())