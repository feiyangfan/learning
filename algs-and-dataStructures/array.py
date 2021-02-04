from typing import *

# Hash map
def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    diff_map = dict()
    for i in range(n):
        diff = target - nums[i]
        if diff not in diff_map:
            diff_map[nums[i]] = i
        else:
            return [diff_map[diff], i]


def twoSumSorted1(nums: List[int], target: int) -> List[int]:
    """
    the input array nums is sorted
    """
    pass


# two-pointer
def twoSumSorted2(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1
