class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter= 0
        for i, v in enumerate(nums):
            if v != val:
                nums[counter] = v 
                counter+=1
        
        return counter


"""
They don't want us to replace the values with sentinel values. 
They actually want them to be removed.

IN PLACE - can't create a new list and return it, must modify the original array
"""