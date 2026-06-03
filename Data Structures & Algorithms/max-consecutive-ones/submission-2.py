class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_streak = 0
        max_streak = 0

        for num in nums:
            if num == 1:
                cur_streak +=1
                max_streak = max(cur_streak, max_streak)
            else:
                cur_streak = 0
        
        return max_streak

        