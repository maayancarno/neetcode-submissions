class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        if len(nums_set) == len(nums):
            return False
        
        return True





# so first, what I would do is convert the list of numbers to a set because that would eliminate any duplicates
# then I would compare the length of the set to the length of the original number list and if they are the same then
# it returns true, and if not it returns false

"""
 O(n) time and O(n) space
"""