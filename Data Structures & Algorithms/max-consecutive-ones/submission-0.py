class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        current_streak=0
        max_streak=0

        for num in nums:
            if num ==1:
                current_streak += 1
            else:
                current_streak = 0
        
            max_streak = max(current_streak, max_streak)
        
        return max_streak



"""
THINKING THROUGH THE PROBLEM
=============================
- Loop throuh array left to right
- At each element, you ask yourself: is this a 1 or a 0? 
- If it's a 1, you increase your current streak count by one. 
- If it's a 0, you reset your current streak count back to zero. 
- After each element, you compare your current streak count to the best you've ever seen.
- If the current one is bigger, that becomes your new best. 
- When you've gone through every element, the best you recorded is your answer.
"""

"""
NOTES
=======

Constraints
1. 1 <= nums.length <= 100,000
    - The first one says the array will always have at least 1 element and at most 100,000 elements. 
    - Means no need to worrry about handling empty array edge case
    - Upper end shows can be larfge so need an efficient solution

2. nums[i] is either 0 or 1
    - Every element in the array is either a 0 or a 1
    - Don't need to hanlde edge cases for other possible valies

"""

