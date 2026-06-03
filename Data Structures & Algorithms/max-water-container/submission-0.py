class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0

        while left < right:
            area = (right - left) * min(heights[right], heights[left])
            max_area = max(area, max_area)

            if heights[left] < heights[right]:
                left +=1
            elif heights[right] < heights[left]:
                right -=1 
            else:
                left +=1
        
        return max_area 





        






"""
You've got two walls of different heights and you're filling water between them. 
The water can only rise as high as the shorter wall before it spills over. 
So the height of your water is determined by the shorter of the two walls.
That's what min(heights[i], heights[j]) gives you — the height of the shorter wall.


Each time u move left forward or right backward the width is shrinking

"""