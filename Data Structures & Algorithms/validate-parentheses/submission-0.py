class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False

        bracket_pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for ch in s:
            if ch in bracket_pairs:
                stack.append(ch)
            elif ch in bracket_pairs.values() and stack and ch == bracket_pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        else:
            return False



            





"""
For every type of opening bracket there must be the same type of closing bracket 
so there must be an equal number of opening brackets and closing brackets for each type

Need to do a dictionary of bracket pairs with the opening bracket as the key and the closing bracket as the value and 
then each pair represents this for the different bracket type and so there will be three pairs in total

ONCE INITIALISED EMPTY STACK
Basically, you need to loop through a string, 
On the first iteration you would need a condition that checks if the stock is empty and if the stack is empty then the 
first character in the string must be a key in the bracket pair dictionary
Then, for the rest of the iterations what you do is ess
"""