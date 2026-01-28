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

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        for i in range(0, len(nums), 2):
            a = nums[i]
            b = nums[i + 1]
            arr.append(b)
            arr.append(a)
        return arr


################### STACK ###################
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {"}": "{", ")": "(", "]": "["}
        for char in s:
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
            else:
                if not stack:
                    return False
                opened = stack.pop()
                if close_to_open[char] != opened:
                    return False
        if not stack:
            return True
        return False


################### 2 POINTERS ###################
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_so_far = 0
        l, r = 0, len(heights) - 1
        while l < r:
            current = (r - l) * min(heights[l], heights[r])
            max_so_far = max(max_so_far, current)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_so_far
    

################### LINKED LIST ###################
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


################### HEAP ###################
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [num for num in nums]
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        self.localvar = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.localvar:
            heapq.heappop(self.heap)
        return self.heap[0]