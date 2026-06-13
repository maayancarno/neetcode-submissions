class Solution:
    def isHappy(self, n: int) -> bool:

        def getSumOfSquares(num:int) -> int:
            sum_squares = 0

            while num > 0:
                d = num % 10
                d_squared = d * d
                sum_squares += d_squared
                num = num//10 
            
            return sum_squares
        
        slow = n
        fast = n

        while True:
            slow = getSumOfSquares(slow)
            fast = getSumOfSquares(getSumOfSquares(fast))  

            if fast == 1:
                return True

            if slow == fast:
                return False



"""

"""
