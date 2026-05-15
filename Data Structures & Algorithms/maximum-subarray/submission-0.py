class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]

        # Running sum of the current subarray.
        curSum = 0

        for n in nums:
            # The key greedy decision: if the running sum went
            # negative, reset to 0 (throw it away, start fresh).
            curSum = max(curSum, 0)

            # Extend the current subarray by adding this element.
            curSum += n

            # If the current subarray is better than anything
            # we've seen before, update the best answer.
            maxSum = max(maxSum, curSum)

        return maxSum