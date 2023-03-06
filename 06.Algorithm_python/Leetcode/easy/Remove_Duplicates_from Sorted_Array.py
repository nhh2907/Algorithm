# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i != (len(nums) - 1):
            if nums[i] == nums[i + 1]:
                del nums[i]
                continue
            i += 1
        return len(nums)

# best
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst = sorted(list(set(nums)))
        for i, j in enumerate(lst):
            nums[i] = j

        return len(lst)
