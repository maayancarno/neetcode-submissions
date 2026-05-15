from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = defaultdict(list)

        for word in strs:
            char_count = [0] * 26

            for letter in word:
                char_count[ord(letter) - ord("a")] += 1

            mappings[tuple(char_count)].append(word)

        return list(mappings.values())


"""

Build the count array (26 zeros, count the letters)
Convert it to a tuple
Use that tuple as a key in a dictionary, and append the word to that key's list
"""
