class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 2
        for i in range(2, len(nums)):
            if nums[ptr-2] != nums[i]:
                nums[ptr] = nums[i]
                ptr +=1
        
        return ptr





"""
SAME STRUCTURE AS REMOVE DUPLICATES EASY
The structure stays the same, I just change the comparison. 
Instead of comparing against the last kept value, 
I compare against the value two slots back, nums[ptr minus 2], and start ptr at 2. 
That allows a value through twice before it starts being treated as a duplicate.
"""