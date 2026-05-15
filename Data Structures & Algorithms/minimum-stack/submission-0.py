class MinStack:

    def __init__(self):
        self.stack =[]
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack and self.min_stack:
            self.stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
    


"""
NOTES FOR GET MIN
==================
The brute force solution would be to build a new list, WHERE YOU WOULD BASICALLY LOOP THROUGH 
THE INPUT AND THEN IF ANY OF THE 
INPUT WAS NOT AN INTEGER, YOU WOULD APPEND IT AS NO AND IF IT WAS A DIGIT YOU WOULD CONVERT THE STRING 
TO AN INTEGER AND THEN APPENDED THE INTEGER TO THE LIST

IF IN INT THEY ASK WHY POPPING FROM MIN AND MAIN:
Because each position in the min stack records the minimum at that point in time, so if 
I remove an element from the main stack without removing its corresponding entry from the min stack, 
the min stack is now answering for a state that no longer exists."

"""
        
