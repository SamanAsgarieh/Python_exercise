'''
Minimum Difference Between Largest and Smallest Value in Three Moves:

Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.
Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.
'''
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        nums.sort()
        return min(nums[-3]-nums[1],nums[-4]-nums[0],nums[-1]-nums[3],nums[-2]-nums[2])