class Solution:
    # Example strs = ["Hello", "World"]

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        
        return encoded_str
        # encoded str = 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s): # The loop runs as long as i is less than the string
            j = i #First iteration j=0
            while s[j] != "#": #s[0] is not equal #it's equal to 5 therefore j is increasd by 1. j = 1
                j += 1

            length = int(s[i:j]) # int(s[0:1]) = 5
            word = s[j+1: j+ 1+length] # First word becomes s[2:7] = Hello
            decoded_str.append(word) # The word is added to the decoded_str List

            i=j+1+length #i is increased to 7

        return decoded_str
