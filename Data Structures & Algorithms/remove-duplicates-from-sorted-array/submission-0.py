class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right -1]:
                nums[left] = nums[right]
                left +=1
        
        return left

        




"""
non-decreasing order - starts with the smallest then gets bigger 
since array i sorted then duplicates will be next to each other

As we iterate through the array from left to right we can check for duplicate values by checking if the current value is the same as the previous one
If it is then it's a duplicate, but if not, then the current value is unique

Each time you encounter a new unique value, you write them back into the same array starting from the beginning
In order to keep track of where we write the next unique value, we use the current position of the left pointer
This is done by each time we encounter a unique value. We move it to be at the position where the left point are currently is and 
then once it's moved we increment the left pointer by one.
right pointer is index that walks through array

We initialise left as 1 because the first element is always unique because there's 
nothing before it to be a duplicate of and so position 0 is already taken care of

You return left itself because, due to zero-indexing, the index of the next empty position is equal to the count of elements already placed.
"""