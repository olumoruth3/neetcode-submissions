class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Using a hash map to store the count of eac character in the 2 strings
        count_s, count_t = {}, {}
        # Filling the hash map
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        print(count_s)
        print(count_t)

        # Compare the frequency of each character in both strings
        for char in count_s:
            # if one unmatching character is found, it immediatel returns False
            if count_s[char] != count_t.get(char, 0):
                return False

        return True
        