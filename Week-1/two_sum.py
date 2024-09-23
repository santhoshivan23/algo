from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for idx, num in enumerate(nums):
            if target - num in visited:
                return [visited[target-num], idx]
            visited[num] = idx
        return []

# https://leetcode.com/problems/two-sum/