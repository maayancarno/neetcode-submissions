class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True


        








"""
# Creates a list of 26 zeros, one slot for each letter of the alphabet. 
        # Index 0 represents 'a', index 1 represents 'b', and so on up to index 25 for 'z'.
        # WHY: ADD IN 
        count = [0] * 26

        for i in range(len(s)):
            # For the character at position i in string s, calculate which alphabet slot it belongs to
            # Convet that character from an to an index from 0 to 25 and then increment that slot by one 
            # because we found this letter in s
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

 TIME COMPLEXITY
 O(n), where n is the length of the strings. 
 You loop through the strings once, and then loop through the count array once — 
 but the count array is always 26 items regardless of how long the strings are, 
 so that's O(26) which is just O(1). So overall it's O(n).           


BRUTE FORCE APPROCAH - BAD
The brute force approach would be to sort both strings alphabetically and then check if they're equal. So "cat" becomes "act" and "tac" becomes "act" — they match, so they're anagrams.
In Python that's literally just return sorted(s) == sorted(t).
It's simple and easy to understand, but the time complexity is O(n log n) because sorting takes O(n log n).

So when an interviewer asks "why is your counting approach better", you'd just say "sorting would be O(n log n), but counting letters only needs one pass through the string, so it's O(n)."

       
"""