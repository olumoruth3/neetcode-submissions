class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key in anagram_groups:
                anagram_groups[key].append(string)
            else:
                anagram_groups[key] = [string]




        return list(anagram_groups.values())

