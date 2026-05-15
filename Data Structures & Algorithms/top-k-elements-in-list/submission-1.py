from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] +=1

        num_by_freq = [[] for i in range(len(nums)+1)]
        
        for num, freq in frequencies.items():
            num_by_freq[freq].append(num)
        
        k_highest = []

        for i in range(len(num_by_freq) - 1, -1, -1):
            if len(k_highest) != k:
                k_highest.extend(num_by_freq[i])
        
        return k_highest

"""
USE .EXTEND TO FLATTEN INSTEAD OF APPEND 
"""