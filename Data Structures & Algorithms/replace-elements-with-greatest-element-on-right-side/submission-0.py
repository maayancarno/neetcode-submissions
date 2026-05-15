class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        current_max = -1 

        for i in range(len(arr)-1, -1, -1):
            # Save original value
            og_val = arr[i]
            # Replace original value with the current max
            arr[i] = current_max
            # Update the running max if the original value at this position was bigger than the current max
            current_max = max(og_val, current_max)
        
        return arr 







"""
NOTES
=====
- "The greatest element among the elements to its right" means: 
    for any element at index i, look at all elements from index i+1 to the end of the array, 
    and find the maximum value among those
- look at each position and then at each value at each position look at all the values afterwards so on the right and then replace it with whatever the largest value is of those on the right and if there is nothing on the right then put it to be minus one
- walking backwards and you're keeping track of the biggest value you've seen so far,
- Replace the current element with the running max (because the running max represents the greatest value to its right — everything you've already visited)
- Update the running max if the original value at this position was bigger than the current max

NEED TO EXPLAIN WNY NOT BRUTE FORCE APPROACH OF LOOPING THROUGH FROM FRONT
"""