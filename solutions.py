################### IMPORTS ###################
from typing import List

################### ARRAYS & HASHING ###################
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        if len(s) != len(t):
            return False
        for char in s:
            mapS[char] = 1 + mapS.get(char, 0)
        for char in t:
            mapT[char] = 1 + mapT.get(char, 0)
        if mapS == mapT:
            return True
        return False
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            # first check if the diff is in there then return
            if (target - num) in hashmap:
                return [hashmap[target - num], i]
            else:
                hashmap[num] = i