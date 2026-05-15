class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # first you create a set, which is the window and the set must be of size less than or equal to K
        window = set()

        # then you initialise the left pointer to start at the beginning of the array
        # L is an index pointer, not a value — we set it to 0 because that's the position 
        # of the first element, 
        # and we use nums[L] whenever we need the actual value at that position.
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False
        






"""
They are saying there are two values a position i am position j 
and the values of each of these positions must be the same.

They can be K width apart from each other at most, 
so can also be a width apart from each other that is less than K the width just cannot be greater than k
Also the fact that the formula uses absolute shows that it doesn't matter which one comes first the only thing that matters really is the difference

"""
