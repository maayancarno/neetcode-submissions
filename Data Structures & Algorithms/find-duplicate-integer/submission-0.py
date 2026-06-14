class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        slow2 = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                while True:
                    slow = nums[slow]
                    slow2 = nums[slow2]

                    if slow == slow2:
                        duplicate = slow
                        return slow



"""
Understanding n
================

array has n+1 integers 
between values 1 to n

e.g. n = 6
contains 7 integers
values can be between 1 and 6 

"""