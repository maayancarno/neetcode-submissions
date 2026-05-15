class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # okay, so what you wanna do is start by initialising what the maximum sum would be and we don't 
        # want to set it to 0 because if there are negative numbers in the list then the rest of the approach 
        # won't work when we are trying to find the maximum because zero will always be greater, 
        # so instead we want to set it to something that is already in the list
        # therefore, we will set it to the value of the element at the first position so that we can also loop through starting
        max_sum = nums[0]
        min_sum = nums[0]

        # then we want to initialise the current sum to 0 and then we can keep track of it throughout
        cur_max_sum = 0
        cur_min_sum = 0
        
        for n in nums:
            cur_max_sum = max(cur_max_sum, 0)
            cur_min_sum = min(cur_min_sum, 0)
            cur_max_sum+= n
            cur_min_sum += n
            max_sum = max(max_sum, cur_max_sum)
            min_sum = min(min_sum, cur_min_sum)
        
        if max_sum < 0:
            return max_sum
        
        total_sum = sum(nums)
        max_wrap_sum = total_sum - min_sum
        return max(max_wrap_sum, max_sum)

            






"""
MY NOTES
=======
They say: the next element of nums[i] is nums[(i + 1) % n]

- Say your array has 5 elements, so n = 5. 
- If you're at the last element (index 4) and you want the "next" element, 
- normally index 5 doesn't exist. 
- But (4 + 1) % 5 = 0, which wraps you back to the beginning. 
- The modulo makes it wrap around.


They say: nums[(i - 1 + n) % n]
- The same thing as above but going backwards. 
- If you're at index 0 and want the previous element, (0 - 1 + 5) % 5 = 4, 
- which takes you to the last element.

APROACH I YHINK
1. Run Kadane's normally to find the max subarray (the non-wrapping case)
2. Run Kadane's again but looking for the minimum subarray
3. Subtract that minimum from the total sum of the array — that gives you the wrapping case
4. Return whichever is bigger

The maximum wrapping subarray is the complement of the minimum non-wrapping subarray. 
So total sum minus minimum subarray gives us the wrapping case, and we compare that against the 
regular Kadane's result.

"""



"""
Initial talkthrough 
====================
Okay, so if they want the maximum possible some of the sub area probably use Kayden's algorithm

The constraint says each element can only appear in the subarray at most once 
— meaning even though the array is circular, the final subarray can't repeat any element. 
This makes sense because if it could, and all elements were positive, you could just keep wrapping around 
adding everything again and the sum would never stop growing

"""