class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        # Count the occurrence of a letter in each string and group together ones with the same character frequencies
        
        for string in strs:
            count = [0] * 26 # a to z
            for char in string:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)
            if key in anagram_groups:
                anagram_groups[key].append(string)
            else:
                anagram_groups[key] = [string]

        return list(anagram_groups.values())

