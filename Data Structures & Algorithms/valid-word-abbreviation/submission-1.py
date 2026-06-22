class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        abbr_ptr = 0
        word_ptr = 0

        while abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                if int(abbr[abbr_ptr]) == 0:
                    zero_start = abbr_ptr == 0
                    zero_after_letter = abbr_ptr > 0 and abbr[abbr_ptr-1].isalpha()
                    if zero_start or zero_after_letter:
                        return False
                else:
                    number = 0
                    while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                        number = number * 10 + int(abbr[abbr_ptr])
                        abbr_ptr += 1
                    word_ptr += number

                    if word_ptr > len(word):
                        return False
            else:
                if word_ptr >= len(word) or abbr[abbr_ptr] != word[word_ptr]:
                    return False
                
                abbr_ptr += 1
                word_ptr += 1
        
        return word_ptr == len(word)
                    
                

                

                    








"""
Edge cases
==========
- leading zeros

if index greater than 0 : # avoid wrap around
    if its digit and is 0 and ch before is not a digit
    if index
"""