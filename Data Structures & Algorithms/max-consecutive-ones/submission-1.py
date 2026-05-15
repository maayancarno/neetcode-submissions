class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current_max = 0
        current_streak = 0

        for num in nums:
            if num == 1:
                current_streak += 1

                current_max = max(current_streak, current_max)
            
            else:
                current_streak = 0

        return current_max

    

"""
So you want to keep track of the current maximum
You also wanna keep track of the current streak
So basically, you wanna loop through the array and at each stage if it's a one you increase the streak by one 
Then you check if the current streak is greater than the maximum and if it is the maximum becomes the current streak

and then if not, you check if the current streak
Is greater than the maximum and if it is then the current maximum becomes the current streak and then the current streak gets reset to 0


EDGE CASE:
Last number nit necessarily a zero so you can't rely on only checking the current streak compared to the max when you hit a zero because if the last streak is the highest and it doesn't end in a zero then it won't wor
"""