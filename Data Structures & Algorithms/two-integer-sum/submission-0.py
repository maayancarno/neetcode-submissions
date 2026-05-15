class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i




"""
Okay, so the brute force approach would be to loop through the array multiple times and each stage you check all the numbers after it to see


Okay, so basically what you wanna do is you want to loop through the array in each stage? You want to culet a compliment which would be the current number minus the target number.
But since we need to return the indexes when the condition is true if the condition does meet true then what we need to do is we also need to keep track of the indexes and so will use a numerat
And essentially what we need to do as we want to check it as we're going through so fast we want to initialise a dictionary
Where we will store all the seen numbers and their indexes as key value pairs where the actual value of the seen number will be the key and the index which that number is in the array will be the value

Checking if something in a_list is O(n) because Python has to scan through the whole list to find it. And you're already inside a loop which is O(n). So that's O(n) × O(n) = O(n²).
Checking if something in a_dictionary is O(1) because dictionaries use hashing — it's an instant lookup. So it's O(n) × O(1) = O(n).

"""